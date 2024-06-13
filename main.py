import requests
import os

api_key = os.getenv("NEWS_API_KEY")
url = (f"https://newsapi.org/v2/top-headlines?country="
       f"us&category=business&apiKey={api_key}")

# make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access article titles
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
