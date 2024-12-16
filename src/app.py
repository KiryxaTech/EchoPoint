# Copyright (c) 2024 EchoPoint.  
# All rights reserved.

from datetime import datetime
from core.logger import setup_logger


class App:

    def __init__(self) -> None:
        self._logger = setup_logger(datetime.now().strftime("%Y-%m-%d %H-%M-%S.log"))

    def start(self) -> None:
        self._logger.info("App started.")
        # Code...

    def stop(self) -> None:
        self._logger.info("App finished.")


if __name__ == "__main__":
    App().start()