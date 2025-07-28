import requests
from bs4 import BeautifulSoup

def scrape():
    url = "https://www.cloudskillsboost.google/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []

    for card in soup.select("a.css-1hzj195"):
        title = card.get_text(strip=True)
        href = card.get("href")
        if not href.startswith("http"):
            href = "https://www.cloudskillsboost.google" + href

        results.append({
            "source": "cloudskillsboost.google",
            "platform": "GCP",
            "title": title,
            "description": "",  # lo puedes expandir más adelante
            "url": href,
            "expires_at": None,
        })

    return results
