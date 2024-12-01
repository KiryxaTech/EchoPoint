# Copyright (c) 2024 EchoPoint.  
# All rights reserved.

from typing import Callable
from vkpymusic import TokenReceiver, Service


class VkAuthenticator:
    CONFIG_PATH = r"C:\Users\kiryx_1zgasrh\Projects\EchoPoint\src\config\apiconf.cfg"

    @property
    def is_auth(self) -> bool:
        return False

    @classmethod
    def auth_with_login(
        cls,
        login: str,
        password: str,
        on_2fa: Callable[[], str] = None
    ) -> None:
        
        token_receiver = TokenReceiver(login, password)
        if token_receiver.auth(on_2fa=on_2fa):
            token_receiver.save_to_config(cls.CONFIG_PATH)

    @classmethod
    def get_service_from_config(cls) -> Service | None:
        return Service.parse_config(cls.CONFIG_PATH)