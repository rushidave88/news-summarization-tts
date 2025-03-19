from transformers import pipeline

MODEL_NAME = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"  # Explicit model
sentiment_pipeline = pipeline("sentiment-analysis", model=MODEL_NAME)

def analyze_sentiment(text):
    result = sentiment_pipeline(text)
    return result[0]['label']  


