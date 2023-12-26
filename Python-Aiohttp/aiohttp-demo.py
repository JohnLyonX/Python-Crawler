import aiohttp
import asyncio


# 异步爬虫
async def mian():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://www.baidu.com') as resp:
            print(resp.status)
            print(await resp.text())


asyncio.run(mian())
