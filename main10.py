import httpx

async with httpx.AsyncClient(http2=True) as client:
    response = await client.get('https://httpbin.org')
    print(response.text)
