# Updated main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from contextlib import asynccontextmanager
from dotenv import load_dotenv
import base64
import requests
import os

## APPLICATION LIFESPAN
# Load the environment variables using FastAPI lifespan event so that they are available throughout the application
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the environment variables
    load_dotenv()
    yield

## FASTAPI APP
# Initialize the FastAPI app
app = FastAPI(lifespan=lifespan)

## PYDANTIC MODELS
# Define a Voice Pydantic model for the request body
class Voice(BaseModel):
    audio_content: str

## FUNCTIONS
# Function to encode the audio
def encode_audio(audio_content):
    return base64.b64encode(audio_content.encode()).decode('utf-8')

# Function to detect emotion and generate emojis
def detect_emotion_and_generate_emoji(audio_content):
    try:
        # Get the base64 string
        base64_audio = encode_audio(audio_content)
        
        # Make a request to the emotion detection API
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.environ['EMOTION_API_KEY']}"
        }

        payload = {
            "audio_content": base64_audio
        }

        response = requests.post("https://api.emotion-analysis.com/detect", headers=headers, json=payload)
        response_data = response.json()
        
        # Process the emotion data and generate emojis
        # Assuming the response_data contains the detected emotion (e.g., "happy", "sad", "angry", etc.)
        # You would write logic here to map emotions to emojis
        
        # For demonstration, let's assume we have a function to generate emojis based on detected emotion
        emojis = generate_emojis(response_data['emotion'])
        
        return emojis
    except Exception as e:
        # Handle errors
        raise HTTPException(status_code=500, detail=str(e))

# Function to generate emojis based on detected emotion
def generate_emojis(emotion):
    # This is just a placeholder function
    # You would replace this with your actual logic to generate emojis based on the detected emotion
    if emotion == "happy":
        return "😊😄🥳"
    elif emotion == "sad":
        return "😢😔😞"
    elif emotion == "angry":
        return "😡😤🤬"
    else:
        return "😐🤔😶"

## FASTAPI ENDPOINTS
## POST - /detect_emotion
# Detect emotion from voice content and generate emojis
@app.post("/detect_emotion")
async def detect_emotion(voice: Voice):
    try:
        # Call the function to detect emotion and generate emojis
        emojis = detect_emotion_and_generate_emoji(voice.audio_content)
        return emojis
    except Exception as e:
        # Handle errors
        raise HTTPException(status_code=500, detail=str(e))
