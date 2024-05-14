import streamlit as st
import speech_recognition as sr
from textblob import TextBlob

# Initialize Speech Recognition
recognizer = sr.Recognizer()

# Function to analyze sentiment and generate emoji
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0.5:
        emoji = "😊"
    elif sentiment_score < -0.5:
        emoji = "😞"
    else:
        emoji = "😐"
    return emoji

# Streamlit app
st.title("Voice-to-Text Chatbot")

# Record voice input
with st.echo():
    st.write("Click the button and speak...")
    try:
        with sr.Microphone() as source:
            st.write("Recording...")
            audio_data = recognizer.record(source, duration=5)  # Adjust duration as needed
            st.write("Processing...")

        # Convert speech to text
        text = recognizer.recognize_google(audio_data)
        st.write(f"You said: {text}")

        # Analyze sentiment and generate emoji
        emoji = analyze_sentiment(text)
        st.write(f"Sentiment: {emoji}")

    except sr.RequestError as e:
        st.error("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        st.error("Could not understand audio")