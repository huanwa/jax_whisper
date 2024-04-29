import replicate
import os



#REPLICATE_API_TOKEN=""


input = {
    "audio": "https://pub-8a6c901f26754c4bbd4f79e70e61d104.r2.dev/luvvoice.com-20240426-0jEx.mp3"
}

output = replicate.run(
    "openai/whisper:4d50797290df275329f202e48c76360b3f22b08d28c196cbc54600319435f8d2",
    input=input
)
texts = [segment.get('text') for segment in output.get('segments', [])]
long_text = ' '.join(text for text in texts if text)
print(long_text)
