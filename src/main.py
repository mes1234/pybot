import asyncio
from asyncio.events import AbstractEventLoop
import time
from  driver.driver import start_debugger
from  eventbus.loop import EventBus

def handler(msg):
    print(f"this is {msg}")

async def blabl():
    while(True):
        print("blalbl")
        await asyncio.sleep(1)

async def run(topic:str):
    eb = EventBus("raspberrypi.local:4222")
    await eb.connect()
    await eb.subscribe(topic,handler=handler)
    while(True):
        await asyncio.sleep(1)

if __name__ == "__main__":


    
    loop = asyncio.get_event_loop()
    tasks = []
    tasks.append(asyncio.ensure_future(run("DEM1")))
    tasks.append(asyncio.ensure_future(blabl()))
    # tasks.append(asyncio.ensure_future(run("DEM2")))
    # tasks.append(asyncio.ensure_future(run("DEM3")))
    loop.run_until_complete(asyncio.wait(tasks))
    
    loop.close()

    # start_debugger()
