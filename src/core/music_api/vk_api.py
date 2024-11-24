# Copyright (c) 2024 EchoPoint.  
# All rights reserved.

from core.music_api.music_api import MusicAPI


class VkMusicAPI(MusicAPI):
    def __init__(self):
        super().__init__("vk_api_token")

    def first_auth(self, login, password):
        pass