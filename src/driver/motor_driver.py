
import json
import asyncio
import logging
from typing import Callable, TypeVar

from msg.motor_command import MotorAction


async def run_motor(queue: asyncio.Queue):
    while True:
        command: MotorAction = await queue.get()
        logging.info(f"Will set {command}")
        pass
        await asyncio.sleep(1)
