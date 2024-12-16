# Copyright (c) 2024 EchoPoint.
# All rights reserved.

import configparser


class TokensConfig:
    """Класс для управления конфигурацией OAuth, включая сохранение и загрузку токена."""
    CONFIG_FILE = r"C:\Users\kiryx_1zgasrh\Projects\EchoPoint\src\config\apiconf.cfg"
    
    @staticmethod
    def save_token(section: str, token: str) -> None:
        config = configparser.ConfigParser()
        config.read(TokensConfig.CONFIG_FILE)
        if section not in config:
            config.add_section(section)
        config[section]['token'] = token
        with open(TokensConfig.CONFIG_FILE, 'w') as configfile:
            config.write(configfile)
    
    @staticmethod
    def load_token(section: str) -> str:
        config = configparser.ConfigParser()
        config.read(TokensConfig.CONFIG_FILE)
        return config.get(section, 'token', fallback=None)