import os
from googleapiclient.discovery import build
import json
#import isodate


# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('You-Tube-API')
youtube = build('youtube', 'v3', developerKey=api_key)
class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str, video_count=0) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.title = None
        self.video_count = video_count
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"

    def get_service():

        return youtube

    def to_json(self, filename):
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        if 'items' in channel and len(channel['items']) > 0:
            channel_data = {
                "id": self.channel_id,
                "name": self.channel_id['items'][0]['snippet']['title'],
                "link": self.url,
                "video_count": self.video_count
            }
            with open(filename, 'a') as file:
                json.dump(channel_data, file)


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(channel)