import streamlit as st
from gtts import gTTS
import os

# 텍스트를 음성으로 변환
text = "안녕하세요 음성비서 프로그램 실습중입니다."
tts = gTTS(text=text, lang="ko")
tts.save("output.mp3")

# 파일이 제대로 생성되었는지 확인
if os.path.exists("output.mp3"):
    st.success("파일이 성공적으로 생성되었습니다.")
    # 스트림릿에서 오디오 파일 재생
    audio_file = open("output.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3")
else:
    st.error("파일 생성에 실패했습니다.")
