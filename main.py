import requests
import os
from send_email import send_email

api_key = os.getenv("NEWS_API_KEY")
url = (f"https://newsapi.org/v2/top-headlines?country="
       f"us&category=business&apiKey={api_key}")

# make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# write article titles and descriptions
with open("draft.txt", 'w') as file:
    for article in content["articles"]:
        file.writelines(article["title"] + '\n')
        try:
            file.writelines(article["description"] + 2*'\n')
        except TypeError:
            file.writelines("(no description given)" + 2*'\n')


with open("draft.txt", 'r') as file:
    message = file.read()
    message = message.encode(encoding='utf-8')


send_email(message)