from whisper_url import WhisperTranscription
from whisper_file import WhisperTranscriptionFile # type: ignore

# 创建WhisperTranscription的实例
# whisper = WhisperTranscription()

# # 调用transcribe_video方法并传入YouTube视频链接
# whisper.transcribe_video("https://www.youtube.com/watch?v=H1YoNlz2LxA")


whisper = WhisperTranscriptionFile()

# 传入音频文件路径
transcribed_text = whisper.transcribe(r'F:\下载\luvvoice.com-20240429-0gEw.mp3')

# 输出转录结果
print("转录结果：", transcribed_text)