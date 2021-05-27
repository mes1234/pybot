import asyncio
import logging
from eventbus.event_bus import run_eventbus
from driver.motor_driver import run_motor

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)


async def main():
    communication_bus = asyncio.Queue()
    tasks = await asyncio.gather(
        run_eventbus(address="raspberrypi.local:4222",
                     topic="DEMO1", queue=communication_bus),
        run_motor(queue=communication_bus))

if __name__ == "__main__":
    asyncio.run(main())
