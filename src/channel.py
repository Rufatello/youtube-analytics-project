import os
from googleapiclient.discovery import build
import json

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('You-Tube-API')
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.title = ""
        self.description = ""
        self.subscriber_count = 0
        self.video_count = 0
        self.view_count = 0
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.print_info()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.channel_id,  part='snippet,statistics').execute()
        self.channel_id = channel['items'][0]['id']
        self.title = channel['items'][0]['snippet']['title'],
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.description = channel['items'][0]['snippet']['description']
        self.view_count = channel['items'][0]['statistics']['viewCount']
        self.subscriber_count = channel['items'][0]['statistics']['subscriberCount']

    @classmethod
    def get_service(cls):
        return youtube

    def to_json(self, filename):
        channel_data = {
            'id': self.channel_id,
            'name': self.title,
            'link': self.url,
            'description': self.description,
            'view_count': self.view_count,
            'subscriber_count': self.subscriber_count

        }
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(channel_data, file, ensure_ascii=False, indent=2)
