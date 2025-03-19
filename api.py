import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from news_scraper import fetch_news
from sentiment_analysis import analyze_sentiment
from comparative_analysis import comparative_analysis
from tts import text_to_speech

app = FastAPI()


os.makedirs("static", exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/analyze/{company}")
async def analyze_news(company: str):
    articles = fetch_news(company)

    # sentiment analysis
    for article in articles:
        article["sentiment"] = analyze_sentiment(article["summary"])

    # Generate comparative sentiment analysis
    sentiment_comparison = comparative_analysis(articles)

    # Convert sentiment report to Hindi speech
    final_text = f"Sentiment Analysis Report: {sentiment_comparison}"
    audio_file = text_to_speech(final_text)

    return {
        "company": company,
        "articles": articles,
        "sentiment_comparison": sentiment_comparison,
        "tts": audio_file if audio_file else None  
    }

@app.get("/audio")
async def get_audio():
    """ Serves the generated audio file """
    audio_path = "static/output.mp3"
    if os.path.exists(audio_path):
        return FileResponse(audio_path, media_type="audio/mpeg")
    return {"error": "Audio file not found"}
