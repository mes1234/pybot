import asyncio

SLEEP = 1


def sleeper(func):
    async def wrapper(*args, **kwargs):
        while True:
            func(*args, **kwargs)
            await asyncio.sleep(SLEEP)
    return wrapper
