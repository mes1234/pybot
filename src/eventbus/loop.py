import asyncio
from asyncio.events import AbstractEventLoop
from typing import Callable
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers


class EventBus:
    '''
    EventBus is a class to interact with NATS server
    '''
    _nc = NATS()
    _loop = None
    _future = None
    _address = ""
    _subscribers = []

    def __init__(self, address: str) -> None:
        self._address = address

    async def connect(self) -> None:
        await self._nc.connect(self._address,self._loop)


    async def subscribe(self, topic: str, handler: Callable) -> None:
        sid = await self._nc.subscribe(topic,cb=self._handler_dispatcher(handler))
        self._subscribers.append(sid)


    def _handler_dispatcher(self,handler):
        async def _handler(msg):
            subject = msg.subject
            reply = msg.reply
            data = msg.data.decode()
            print("Received a message on '{subject} {reply}': {data}".format(
            subject=subject, reply=reply, data=data))
            handler(data)
        return _handler
