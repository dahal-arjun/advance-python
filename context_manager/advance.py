import asyncio
import aiohttp
"""
Implementing  Context Manager API
"""


class ContextManager:
    def __enter__(self):
        print("Entering the Context Manager")
        return "Testing Context Manager"

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving")


with ContextManager() as ctx:
    print(ctx)


"""
Asynchronous Context Manager
"""


class AsyncContenxtManager:
    def __init__(self, url):
        self._url = url

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        response = await self.session.get(self._url)
        return response

    async def __aexit__(self, exec_type, exc_value, exc_tb):
        await self.session.close()


async def check(url):
    async with AsyncContenxtManager(url) as response:
        html = await response.text()
        print(html)


async def main():
    await asyncio.gather(
            check("https://google.com"),
            check("https://facebook.com"),
        )

asyncio.run(main())
