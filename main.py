import requests
import os
from send_email import send_email

topic = "archaeology"

api_key = os.getenv("NEWS_API_KEY")
url = (f"https://newsapi.org/v2/everything?"
       f"q={topic}"
       f"&apiKey={api_key}"
       f"&language=en")

# make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# write article titles and descriptions
body = ""

for article in content["articles"][:20]:
   if article["title"] is not None:
       body = body + article["title"] + '\n'
   if article["description"] is not None:
       body = body + article["description"] + '\n'
   body = body + article["url"] + 2*'\n'


message = f"""\
Subject: Your {topic} news for today

{body}
"""

message = message.encode(encoding='utf-8')
send_email(message=message)