import httpx
import asyncio


async def fetch(url):
    async with httpx.AsyncClient(http2=True) as client:
        response = await client.get(url)
        print(response.text)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(fetch('https://httpbin.org/get'))
