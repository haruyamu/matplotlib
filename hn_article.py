import requests
import json

url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
response_dict = r.json()
