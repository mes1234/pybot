import logging


class Driver:
    current = 0

    def __init__(self) -> None:
        pass

    def send_new_settings(self, point: int):
        if self.current != point:
            logging.info(f"Sent to device :{point}")
        else:
            logging.info(f"Not needed update :{point}")
        self.current = point
