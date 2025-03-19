import requests

NEWS_API_KEY = "your_newsapi_key_here"

def fetch_news(company_name):
    url = f"https://newsapi.org/v2/everything?q={company_name}&apiKey={'f8f4ab9e37e2451a940c6e32d43c5373'}"
    response = requests.get(url)
    data = response.json()

    articles = []
    for article in data.get("articles", [])[:10]:
        articles.append({
            "title": article["title"],
            "summary": article["description"],
            "text": article["content"]
        })

    return articles
