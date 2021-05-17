import httpx
client = httpx.Client(http2=True)

response = client.get(
    'https://spa16.scrape.center/')
print(response.text)
