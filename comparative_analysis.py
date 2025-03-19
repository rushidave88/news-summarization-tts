from collections import Counter

def comparative_analysis(articles):
    sentiment_counts = Counter([article["sentiment"] for article in articles])
    
    return {
        "Positive": sentiment_counts.get("POSITIVE", 0),
        "Negative": sentiment_counts.get("NEGATIVE", 0),
        "Neutral": sentiment_counts.get("NEUTRAL", 0),
    }
