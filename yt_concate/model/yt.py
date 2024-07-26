import os

from yt_concate.settings import CAPTIONS_DIR


class YT:
    def __init__(self, url):
        self.url = url
        self.id = self.get_video_id_from_url(self.url)
        self.caption_filepath = self.get_caption_filepath()



    @staticmethod
    def get_video_id_from_url(url):
        return url.split('watch?v=')[-1]

    def get_caption_filepath(self, url):
        return os.path.join(CAPTIONS_DIR, self.get_video_id_from_url(self.url) + 'txt')