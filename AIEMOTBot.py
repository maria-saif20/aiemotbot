import streamlit as st
import requests
import tempfile
import validators
import os
from utils import setup_logging, log_error

# Custom CSS
with open('styles.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Setup Logging
setup_logging()

## FUNCTIONS

# Define function for voicetoemotion page
def voicetoemotion():
    st.title("Voice to Emotion")
    st.subheader("Upload your voice file and detect emotions")

    uploaded_voice = st.file_uploader("Upload a voice file", type=["wav"])

    if uploaded_voice:
        st.audio(uploaded_voice, format='audio/wav')
        if st.button("Detect Emotion"):
            with st.spinner("Detecting emotion..."):
                voice_path = save_uploaded_voice(uploaded_voice)
                emotion = detect_emotion_from_voice(voice_path)
                if emotion:
                    st.success(f"Emotion detected: {emotion}")
                else:
                    st.error("Failed to detect emotion.")
import streamlit as st
from utils import detect_emotion_from_voice

# LOGO and TITLE
# -------------------------------------------------------------------------------------------
# Show the logo and title side by side
col1, col2 = st.columns([1, 4])
with col1:
    st.image("AIEMOTBOT.png", use_column_width=True,)
with col2:
    st.title("Hi, I am AIEMOTBOT - Your Emotional AI Assistant!")

# Main content
st.header("Upload your voice file and let me detect the emotion!")
st.subheader("Supported audio formats: WAV, MP3, etc.")

# Function to detect emotion from voice
def detect_emotion():
    uploaded_file = st.file_uploader("Upload a voice file", type=["wav", "mp3"])
    if uploaded_file:
        st.audio(uploaded_file, format='audio/wav')
        if st.button("Detect Emotion"):
            with st.spinner("Detecting emotion..."):
                emotion = detect_emotion_from_voice(uploaded_file)
                if emotion:
                    st.success(f"Emotion detected: {emotion}")
                else:
                    st.error("Failed to detect emotion.")

# Call the function to detect emotion
detect_emotion()

## WEBSITE LINK
## -------------------------------------------------------------------------------------------
# Load the website content, then save it into a vector store, and enable the input field to 
# ask a question
st.session_state['uploaded_link'] = False
if website_link is not None:
    if website_link:
        # Ensure that the user has entered a correct URL
        if validators.url(website_link):
            try:
                # Send POST request to a FastAPI endpoint to scrape the webpage and load its text 
                # into a vector store
                FASTAPI_URL = f"http://localhost:8000/load_link/{llm}"
                data = {"website_link": website_link}
                with st.spinner("Loading website..."):
                    response = requests.post(FASTAPI_URL, json=data)
                    st.success(response.text)
                    st.session_state['current_website'] = website_link
                    st.session_state['uploaded_link'] = True
                    st.switch_page("pages/Web-chat.py")
            except Exception as e:
                log_error(str(e))
                st.switch_page("pages/error.py")
        else:
            st.error("Invalid URL. Please enter a valid URL.")