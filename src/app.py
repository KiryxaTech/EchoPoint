# Copyright (c) 2024 EchoPoint.  
# All rights reserved.

from datetime import datetime
import webbrowser

from core.logger import setup_logger
from yandex_music import Client


class App:
    def __init__(self) -> None:
        self._logger = setup_logger(datetime.now().strftime("%Y-%m-%d %H-%M-%S.log"))
        self._app_thread = None

    def start(self) -> None:
        self._logger.info("App started.")

    def stop(self) -> None:
        self._app_thread = None
        self._logger.info("App finished.")


if __name__ == "__main__":
    App().start()