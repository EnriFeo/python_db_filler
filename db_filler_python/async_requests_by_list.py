import aiohttp
import asyncio

class Async_req_from_list:

    
    @staticmethod
    def get(lista: list[str]):
        return asyncio.get_event_loop().run_until_complete(Async_req_from_list.__async_request_by_list(lista, True))
    
    @staticmethod
    def post(lista: list[str]):
        return asyncio.get_event_loop().run_until_complete(Async_req_from_list.__async_request_by_list(lista, False))
    
    @staticmethod
    async def __get_result(session: aiohttp.ClientSession, url: str):
        async with session.get(url) as resp:
            return await resp.text()

    @staticmethod
    async def __post_result(session: aiohttp.ClientSession, url: str, data):
        async with session.post(url, data = data) as resp:
            return await resp.text()
    
    @staticmethod
    async def __async_request_by_list(lista: list, get: bool):

        async with aiohttp.ClientSession() as session:

            tasks = []
            for url in lista:
                if get:
                    tasks.append(asyncio.ensure_future(Async_req_from_list.__get_result(session, url)))
                else:
                    tasks.append(asyncio.ensure_future(Async_req_from_list.__post_result(session, url['url'], url['data'])))

            return await asyncio.gather(*tasks)
