import requests
import json


query = str(input("What news do you want to see: "))
response = requests.get(f"https://newsapi.org/v2/everything?q={query}&from=2023-05-14&sortBy=publishedAt&apiKey=902285f64e0b4ddd95ec3ed0174363e2")

news = json.loads(response.text)
print(type(news["articles"]))

for article in news["articles"]:
    print("title-->",article["title"])
    print("description-->",article["description"])
    print("------------------------------------------------")
