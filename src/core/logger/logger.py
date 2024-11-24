# Copyright (c) 2024 EchoPoint.  
# All rights reserved.

import logging

# Настройка главного логгера
def setup_logger(file_name):
    logger = logging.getLogger("main")
    logger.setLevel(logging.DEBUG)

    # Создание обработчика для вывода в консоль
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(f"C:\\Users\\kiryx_1zgasrh\\Projects\\EchoPoint\\log\\{file_name}")
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger