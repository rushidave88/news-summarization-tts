import gradio as gr
import requests

def analyze_news(company):
    try:
        response = requests.get(f"http://127.0.0.1:8000/analyze/{company}")
        data = response.json()

        audio_file = "static/output.mp3" if "tts" in data else None

        return data, audio_file
    except Exception as e:
        return {"error": f"Failed to connect to API: {str(e)}"}, None

iface = gr.Interface(
    fn=analyze_news,
    inputs=gr.Textbox(label="Company Name"),
    outputs=[gr.JSON(label="Analysis Report"), gr.Audio(type="filepath", label="Play Hindi Speech")]
)

iface.launch()
