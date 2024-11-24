# Copyright (c) 2024 EchoPoint.  
# All rights reserved.

import logging
from abc import ABC, abstractmethod
from configparser import ConfigParser


logger = logging.getLogger(__name__)


class MusicAPI(ABC):
    def __init__(self, token_name):
        self.token_name = token_name
        self.__token = None

    @abstractmethod
    def first_auth(self, login, password):
        logger.info("Auth in API service.")
        pass

    def _save_token(self, token):
        config = ConfigParser()
        # Читаем конфигурационный файл
        config.read("config\\config.cfg")
        
        # Присваиваем новый токен
        config.set('tokens', self.token_name, token)

        # Открываем файл для записи и сохраняем изменения
        with open("config\\config.cfg", 'w') as configfile:
            config.write(configfile)
            logger.info(f"Token {self.token_name} saved successfully.")