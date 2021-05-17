import requests


url = 'https://spa16.scrape.center/'
response = requests.get(url)
print(response.json())
