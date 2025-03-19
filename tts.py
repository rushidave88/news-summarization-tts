from gtts import gTTS
import os

def text_to_speech(text, language="hi"):
    try:
        os.makedirs("static", exist_ok=True)  
        audio_path = "static/output.mp3"
        tts = gTTS(text, lang=language)
        tts.save(audio_path)
        return audio_path  
    except Exception as e:
        print(f"Error generating speech: {e}")
        return None
