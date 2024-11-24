# Copyright (c) 2024 EchoPoint.  
# All rights reserved.

from core.music_api.music_api import MusicAPI


class YandexMusicAPI(MusicAPI):
    def __init__(self) -> None:
        super().__init__("yandex_api_token")

    def first_auth(self, login, password):
        pass