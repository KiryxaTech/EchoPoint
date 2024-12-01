# Copyright (c) 2024 EchoPoint.  
# All rights reserved.

from vkpymusic import Service
from vkpymusic.models import Song


class VkUserInfo:
    def __init__(self, service: Service) -> None:
        self.__service = service
        self.__user_info = self.__service.get_user_info()

        self.firstname = self.__user_info.first_name
        self.lastname = self.__user_info.last_name
        self.photo = self.__user_info.photo
        self.userid = self.__user_info.userid
        self.songs: list[Song] = None

    def update_songs(self) -> None:
        songs_count = self.__service.get_count_by_user_id(self.userid)
        self.songs = self.__service.get_songs_by_userid(self.userid, songs_count)