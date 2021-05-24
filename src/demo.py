import asyncio
import time
from asyncio.events import TimerHandle
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers

async def run(loop):
    nc = NATS()

    await nc.connect("raspberrypi.local:4222", loop=loop)

    async def message_handler(msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()
        print("Received a message on '{subject} {reply}': {data}".format(
            subject=subject, reply=reply, data=data))

    # Simple publisher and async subscriber via coroutine.
    sid = await nc.subscribe("DEMO", cb=message_handler)


    await asyncio.sleep(100, loop=loop)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    loop.close()
