from fastapi import APIRouter
import requests

router = APIRouter()

@router.get("/{query}")
def get_news(query: str):
    url = f"https://newsdata.io/api/1/news?apikey=pub_f7b7a291182b4a80a2971b053734396a&q={query}&language=en&category=business"
    response = requests.get(url)
    data = response.json()
    
    articles = []
    if "results" in data:
        for article in data["results"][:5]:
            articles.append({
                "title": article.get("title"),
                "description": article.get("description"),
                "url": article.get("link"),
                "published": article.get("pubDate")
            })
    return articles