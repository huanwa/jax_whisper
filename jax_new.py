from gradio_client import Client
import base64
import threading
import os

# make sure this URL matches your http web address
API_URL = "https://sanchit-gandhi-whisper-jax.hf.space/" # if using port 7860
#API_URL = "https://NGROK-ADDRESS.ngrok.io/" # if using ngrok

# set up the Gradio client
client = Client(API_URL)

def transcribe_audio(audio_path, task="transcribe", return_timestamps=False):
    """Function to transcribe an audio file using our endpoint"""
    text, runtime = client.predict(
        audio_path,
        task,
        return_timestamps,
        api_name="/predict_1",
    )
    return text

# transcribe an audio file using our endpoint
# audio_path = r'F:\下载\luvvoice.com-20240414-ZHU6.mp3'
# with open(audio_path, 'rb') as audio_file:
#         base64_audio = base64.b64encode(audio_file.read()).decode('utf-8')
output = transcribe_audio("https://www.youtube.com/watch?v=m8u-18Q0s7I")
print(output)

# transcribe with timestamps
#output_with_timestamps = transcribe_audio("audio.mp3", return_timestamps=True)