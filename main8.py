import httpx
client = httpx.Client(http2=True)

response = client.get(
    'https://httpbin.org/get')
print(response.text)
print(response.http_version)
