from pathlib import Path
from google.cloud import texttospeech
from openai import OpenAI
import warnings

def create_file_directory():
    # Create a directory to save the audio files
    audio_dir = Path(__file__).parent / "audio_files"
    audio_dir.mkdir(parents=True, exist_ok=True)

def text_to_speech(input_text, text_label, provider="google"):
    create_file_directory()
    audio_file_path = Path(__file__).parent / "audio_files" / f"{text_label}.mp3"

    if provider == "google":
        google_client = texttospeech.TextToSpeechClient()

        synthesis_input = texttospeech.SynthesisInput(text=input_text)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Studio-O",
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            speaking_rate=1,
            pitch=0,
        )

        response = google_client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        with open(audio_file_path, "wb") as audio_file:
            audio_file.write(response.audio_content)

    elif provider == "openai":
        openai_client = OpenAI()
        response = openai_client.audio.speech.create(
            model="tts-1",
            voice="shimmer",
            input=input_text
        )

        response.stream_to_file(audio_file_path)

    else:
        raise ValueError("Invalid provider specified.")

    print(f"Audio content for '{text_label}' written to file.")

# # Example usage:
# text_to_speech("Hello, this is a test.", "hello_google", provider="google")
# text_to_speech("Hello, this is a test.", "hello_openai", provider="openai")
