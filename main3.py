import httpx

response = httpx.get('https://httpbin.org/get')
print(response.status_code)
print(response.headers)
print(response.text)
