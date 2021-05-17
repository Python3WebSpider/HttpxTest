import httpx

with httpx.Client() as client:
    response = client.get('https://httpbin.org/get')
    print(response)


client = httpx.Client()
try:
    response = client.get('https://httpbin.org/get')
finally:
    client.close()
