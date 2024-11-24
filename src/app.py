# Copyright (c) 2024 EchoPoint.  
# All rights reserved.

from datetime import datetime
from threading import Thread

from core.logger import setup_logger


class App:
    def __init__(self) -> None:
        self._logger = setup_logger(datetime.now().strftime("%Y-%m-%d %H-%M-%S.log"))
        self._app_thread = None

    def start(self) -> None:
        self._logger.info("App started.")

    def start_in_thread(self) -> None:
        self._app_thread = Thread(target=self.start, daemon=True)
        self._app_thread.start()

    def stop(self) -> None:
        self._app_thread = None
        self._logger.info("App finished.")


if __name__ == "__main__":
    app = App()
    app.start_in_thread()
    app.stop()