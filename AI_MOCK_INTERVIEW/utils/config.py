import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID","Amelia")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")
if not ELEVENLABS_API_KEY:
    raise ValueError("ELEVENLABS_API_KEY is not set in the environment variables.")
if not ELEVENLABS_VOICE_ID:
    raise ValueError("ELEVENLABS_VOICE_ID is not set in the environment variables.")    

RECORDING_DURATION = 10  # in seconds, adjust as needed
SAMPLE_RATE = 44100
AUDIO_FILE_PATH = "recorded_audio.wav"  
RECORDING_CHANNELS = 1  # Mono recording