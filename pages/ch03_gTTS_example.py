from gtts import gTTS
import os

tts = gTTS(text="안녕하세요 음성비서 프로그램 실습중입니다.",lang="ko")
tts.save("output.mp3")

# 파일이 제대로 생성되었는지 확인
if os.path.exists("output.mp3"):
    print("파일이 성공적으로 생성되었습니다.")
else:
    print("파일 생성에 실패했습니다.")
