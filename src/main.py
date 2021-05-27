import asyncio
from asyncio.events import AbstractEventLoop
from asyncio.tasks import create_task
import time
from driver.driver import start_debugger
from eventbus.loop import EventBus


def handler(msg,queue:asyncio.Queue):
    queue.put_nowait(msg)


async def blabl(queue: asyncio.Queue):
    while(True):
        msg = await queue.get()
        print(msg)
        await asyncio.sleep(1)


async def run(topic: str, queue: asyncio.Queue):
    eb = EventBus("raspberrypi.local:4222")
    await eb.connect()
    await eb.subscribe(topic, handler=handler, queue=queue)
    while(True):
        await asyncio.sleep(1)


async def main():
    queue = asyncio.Queue()
    tasks = await asyncio.gather(run("DEMO1",queue), blabl(queue))

if __name__ == "__main__":
    asyncio.run(main())
