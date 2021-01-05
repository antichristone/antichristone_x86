from typing import Optional
from aiohttp import ClientSession

_session: Optional[ClientSession] = None


async def get_session():
    global _session
    if isinstance(_session, ClientSession) and not _session.closed:
        return _session
    _session = ClientSession()
    return _session

async def close_session():
    global _session
    if isinstance(_session, ClientSession) and not _session.closed:
        await _session.close()


async def options_url(URL, headers, data=None, json=None, params=None):
    session = await get_session()
    async with session.options(URL, headers=headers, data=data, json=json, params=params, timeout=1) as response:
        pass

async def options_data_url(URL, headers, data=None, json=None, params=None):
    try:
        await options_url(URL, headers, data, json, params)
    except Exception:
        pass

    await close_session()


async def post_url(URL, headers, data=None, json=None, params=None):
    session = await get_session()
    async with session.post(URL, headers=headers, data=data, json=json, params=params, timeout=1) as response:
        pass

async def post_data_url(URL, headers, data=None, json=None, params=None, timeout=1):
    try:
        await post_url(URL, headers, data, json, params)
    except Exception:
        pass

    await close_session()


async def get_url(URL, headers, data=None, json=None, params=None):
    session = await get_session()
    async with session.get(URL, headers=headers, data=data, json=json, params=params, timeout=1) as response:
        return await response.text()

async def get_data_url(URL, headers, data=None, json=None, params=None):
    try:
        body=await get_url(URL, headers, data, json, params)
    except Exception:
        pass

    await close_session()

    return body

#
