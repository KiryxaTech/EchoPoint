# Copyright (c) 2024 EchoPoint.
# All rights reserved.

import subprocess
import webbrowser
from requests import post
from urllib.parse import urlencode

from web import YandexServer

from core.utils import TokensConfig


class TokenHandler:
    """Класс для обработки токенов: получения и обновления."""
    TOKEN_URL = "https://oauth.yandex.ru/token"
    
    @staticmethod
    def fetch_token(auth_code: str, client_id: str, client_secret: str, redirect_uri: str) -> dict:
        data = {
            'grant_type': 'authorization_code',
            'code': auth_code,
            'client_id': client_id,
            'client_secret': client_secret,
            'redirect_uri': redirect_uri
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = post(TokenHandler.TOKEN_URL, data=urlencode(data), headers=headers)
        response.raise_for_status()
        return response.json()



class YandexAuthenticator:
    CLIENT_ID = "930f4c7db50048e1b84eaaa5af4fa53e"
    CLIENT_SECRET = "e48189abfe4440c38f504ceaaf4fb785"
    REDIRECT_URI = "http://127.0.0.1:4545/"
    BASE_AUTH_URL = "https://oauth.yandex.ru/authorize"

    @classmethod
    def process_token(cls, auth_code: str) -> str:
        """
        Обрабатывает код авторизации, обменивает его на токен и сохраняет.
        Возвращает HTML-контент для отображения в браузере.
        """
        try:
            # Обмен авторизационного кода на токен
            token_data = TokenHandler.fetch_token(
                auth_code,
                cls.CLIENT_ID,
                cls.CLIENT_SECRET,
                cls.REDIRECT_URI
            )
            access_token = token_data['access_token']

            # Сохранение токена
            TokensConfig.save_token('Yandex', access_token)

            # Возвращение HTML-контента
            with open(r"C:\Users\kiryx_1zgasrh\Projects\EchoPoint\src\templates\index.html", "r", encoding="utf-8") as htmlfile:
                return htmlfile.read()
        except Exception as e:
            raise Exception(f"Ошибка при обработке токена: {e}")

    @classmethod
    def oauth(cls) -> None:
        """
        Настраивает и запускает процесс авторизации через OAuth.
        """
        # Создаём и конфигурируем сервер
        server = YandexServer(
            client_id=cls.CLIENT_ID,
            client_secret=cls.CLIENT_SECRET,
            redirect_uri=cls.REDIRECT_URI,
            base_auth_url=cls.BASE_AUTH_URL,
            process_token=cls.process_token
        )

        # Запускаем сервер в отдельном потоке
        webbrowser.open("http://127.0.0.1:4545")
        server.run()