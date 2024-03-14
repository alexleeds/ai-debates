from pathlib import Path
from google.cloud import texttospeech
from openai import OpenAI
import warnings

def openai_text_to_speech(input_text, text_label):
    openai_client = OpenAI()
    
    response = openai_client.audio.speech.create(
    model="tts-1",
    voice="shimmer",
    input=input_text
    )

    # Manage unwanted deprecation warnings 
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    
    speech_file_path = Path(__file__).parent / (text_label+".mp3")
    response.stream_to_file(speech_file_path)

    print('Audio content for ' + text_label + ' written to file.')

def google_cloud_text_to_speech(input_text, text_label):

    google_client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=input_text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
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
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    # The response's audio_content is binary.
    with open(text_label+".mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content for ' + text_label + ' written to file.')