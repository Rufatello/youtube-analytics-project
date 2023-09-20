import os
from googleapiclient.discovery import build

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('You-Tube-API')
youtube = build('youtube', 'v3', developerKey=api_key)
class Video:
    """Класс для ютуб-канала"""

    def __init__(self, video_id) -> None:
        self.video_id = video_id
        video = youtube.videos().list(id=self.video_id, part='snippet,statistics').execute()
        video_data = video['items'][0]
        self.name = video_data['snippet']['title']
        self.url = f'https://www.youtube.com/video/{video_id}'
        self.count_view = video_data['statistics']['viewCount']
        self.like = video_data['statistics']['likeCount']

    def __str__(self):
        return f'{self.name}'



class PLVideo(Video):
    def __init__(self, video_id, id_playlist):
        super().__init__(video_id)
        self.id_playlist = id_playlist

    def __str__(self):
        return f'{self.name}'

