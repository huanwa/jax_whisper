import websocket
import json
import random
import string

def generate_session_hash():
    # 类似于JavaScript中Math.random().toString(36).substring(2);
    # 随机生成一个足够长的字符串作为session_hash
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

# 生成session_hash
session_hash = generate_session_hash()
# 假定 fn_index 是已知的固定值
FN_INDEX = 6

def on_message(ws, message):
    print("Received message:", message)
    response = json.loads(message)
    
    if response['msg'] == 'send_hash':
         ws.send(json.dumps({"fn_index": FN_INDEX, "session_hash":session_hash}))
    elif response['msg'] == 'send_data':
        data_to_send = {
            "data": ["https://www.youtube.com/watch?v=m8u-18Q0s7I", "transcribe", False],
            "event_data": None,
            "fn_index": FN_INDEX,
            "session_hash": session_hash,
        }
        ws.send(json.dumps(data_to_send))
    elif response['msg'] == 'process_completed':
        print("Processing completed:")
        data = response.get('output', {}).get('data', [])
        # 检查数组长度，确保它包含足够的元素
        if len(data) > 1:
            # 第二个元素通常包含转录的文字
            transcribed_text = data[1]
            print("Transcribed text:")
            print(transcribed_text)
        # 服务器通知客户端处理已完成，可以关闭连接
        ws.close()

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
