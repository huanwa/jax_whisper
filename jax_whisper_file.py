import websocket
import json
import random
import string
import base64
import threading
import os
def generate_session_hash():
    # 类似于JavaScript中Math.random().toString(36).substring(2);
    # 随机生成一个足够长的字符串作为session_hash
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

# 生成session_hash
session_hash = generate_session_hash()
# 假定 fn_index 是已知的固定值
FN_INDEX = 3


def on_message(ws, message):
    print("Received message:", message)
    response = json.loads(message)
    
    if response['msg'] == 'send_hash':
        # 请求发生的hash值，发送 session_hash
        ws.send(json.dumps({"fn_index": FN_INDEX, "session_hash":session_hash}))
    elif response['msg'] == 'send_data':
        # 得到 send_data 的消息后，准备发送数据
        # 我们应该在此处处理音频文件的上传，以下假设音频数据存储在 data_to_send 中
        threading.Thread(target=upload_audio, args=(ws,)).start()
    elif response['msg'] == 'process_completed':
        # 处理转录完成的消息
        print("Processing completed:")
        data = response.get('output', {}).get('data', [])
        if len(data) > 1:
            transcribed_text = data[0]
            print("Transcribed text:", transcribed_text)
        ws.close()

def upload_audio(ws):
    # 这里我们将音频数据转换为 base64编码的字符串
    audio_path = r'F:\下载\luvvoice.com-20240414-ZHU6.mp3'  # 你音频文件的路径
    with open(audio_path, 'rb') as audio_file:
        base64_audio = base64.b64encode(audio_file.read()).decode('utf-8')
    
    filename = os.path.basename(audio_path)
    
    data_to_send = {
        "data": [
            {
                "data": f"data:audio/mpeg;base64,{base64_audio}",
                "name": filename
            },
            "transcribe",
            False
        ],
        "event_data": None,
        "fn_index": FN_INDEX,
        "session_hash": session_hash,
    }
    
    ws.send(json.dumps(data_to_send))

def on_error(ws, error):
    print("Error:", error)

def on_close(ws, close_status_code, close_msg):
    print("Closed WebSocket connection.")

def on_open(ws):
    print("WebSocket connection established.")

# WebSocket URL
ws_url = "wss://sanchit-gandhi-whisper-jax.hf.space/queue/join"

# Create a WebSocket application
ws_app = websocket.WebSocketApp(ws_url, on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

# Start the WebSocket client
ws_app.run_forever()
