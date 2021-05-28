
from asyncio.tasks import sleep
import json
import asyncio
import logging
from types import coroutine
from typing import Callable, TypeVar

from msg.motor_command import MotorAction
from driver.scheduler import Scheduler
from driver.driver import Driver
from common.sleeper import SLEEP, sleeper


async def run_motor(queue: asyncio.Queue):
    scheduler = Scheduler(-1, 0)
    driver = Driver()
    while True:
        if not queue.empty():
            command: MotorAction = await queue.get()
            logging.info(f"Will set {command}")
            scheduler.setup(command.time_ms, command.power)
        driver.send_new_settings(next(scheduler))
        await asyncio.sleep(SLEEP)
