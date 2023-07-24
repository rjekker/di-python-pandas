import requests

apiKey = "80559f68dddf48a689a7d5d5d9074522"
r = requests.get(f'https://newsapi.org/v2/top-headlines?country=nl&apiKey={apiKey}')
data = r.json()
print(data['articles'][0]['title'])
