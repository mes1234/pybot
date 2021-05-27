import asyncio
import logging
import json
from asyncio.events import AbstractEventLoop
from typing import Callable, TypeVar
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers

from msg.motor_command import MotorAction


async def run_eventbus(address: str, topic: str, queue: asyncio.Queue):
    eb = EventBus(address=address)
    await eb.connect()
    await eb.subscribe(topic, queue=queue)
    while(True):
        await asyncio.sleep(1)


class EventBus:
    '''
    EventBus is a class to interact with NATS server
    '''
    _nc = NATS()
    _loop = None
    _future = None
    _address = ""
    _subscribers = []
    _queue = None

    def __init__(self, address: str) -> None:
        self._address = address

    async def connect(self) -> None:
        await self._nc.connect(self._address, self._loop)

    async def subscribe(self, topic: str, queue: asyncio.Queue) -> None:
        self._queue = queue
        sid = await self._nc.subscribe(topic, cb=self.msg_handler)
        self._subscribers.append(sid)

    async def msg_handler(self, msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()
        logging.info(f"Recieved msg {subject} {reply}: {data}")
        command = deserialize(data, MotorAction)
        await self._queue.put(command)


T = TypeVar('T')


def deserialize(raw: str, cls: T) -> T:
    raw_dict = json.loads(raw)
    data = cls(**raw_dict)
    return data
