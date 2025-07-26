import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
from elevenlabs.client import ElevenLabsClient
from elevenlabs import generate, play, set_api_key, voices, save, VoiceSettings
import numpy as np
import time
import os
from utils.config import (
    ELEVENLABS_API_KEY, 
    ELEVENLABS_VOICE_ID, 
    SAMPLE_RATE, 
    AUDIO_FILE_PATH, 
    RECORDING_CHANNELS,
)
# Initialize ElevenLabs client

try:
    el_client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
except Exception as e:
    print(f"Error initializing ElevenLabs client: {e}")

r = sr.Recognizer()

def speak_text(text: str):
    """Uses ElevenLabs to convert text to speech and play it."""
    if not el_client:
        print("ElevenLabs client is not initialized.")
        print("Fallback: Printing text instead of speaking.")
        print(f"Interviewer: {text}")
        time.sleep(len(text.split()) / 3)  # Simulate speaking duration
        return

    try:
        print("Generating audio...")
        voice_obj= Voice(
            voice_id=ELEVENLABS_VOICE_ID,
            settings=VoiceSettings(
                stability=0.6,
                similarity_boost=0.75,
                style=0.1,
                use_speaker_boost=True,
            )
        )
        audio = el_client.generate(
            text=text,
            voice=voice_obj,
            model="eleven_multilingual_v2"
        )
        print("Speaking...")
        play(audio)
        print("Finished speaking.")
    except Exception as e:
        print(f"Error during ElevenLabs TTS: {e}")
        print("Fallback: Printing text instead of speaking.")
        print(f"Interviewer: {text}")
        time.sleep(len(text.split()) / 3)
#BELOW IS PRODUCTION IMPROVEMENT

def record_audio(duration: int = 15, filename: str = AUDIO_FILE_PATH) -> str | None:
    """Records audio for a specified duration and saves it to a file."""
    print(f"Recording audio for {duration} seconds...")
    try:
        audio_data = sd.rec(int(duration * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=RECORDING_CHANNELS, dtype='int16')
        sd.wait()  # Wait until recording is finished
        sf.write(filename, audio_data, SAMPLE_RATE)
        print(f"Audio recorded and saved to {filename}")
    except Exception as e:
        print(f"Error during audio recording: {e}")
        return None
    return filename

def transcribe_audio(filename: str) -> str | None:
    """Transcribes audio from a file using speech recognition."""
    print(f"Transcribing audio from {filename}...")
    try:
        with sr.AudioFile(filename) as source:
            audio = r.record(source)  # Read the entire audio file
            transcription = r.recognize_google(audio)
            print(f"Transcription: {transcription}")
    except Exception as e:
        print(f"Error during audio transcription: {e}")
        return None
    return transcription        
