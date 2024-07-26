import urllib.request
import ssl
import json
import requests
import certifi


from yt_concate.settings import API_KEY
from yt_concate.pipeline.steps.step import Step


class GetVideoList(Step):  # class命名規則：駝峰式命名
    def process(self, data, inputs, utils):
        channel_id = inputs['channel_id']

        if utils.video_list_file_exists(channel_id):
            print('找到影片清單')
            return self.read_file(utils.get_video_list_filepath(channel_id))

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(API_KEY,
                                                                                                            channel_id)

        # context = ssl.create_default_context(cafile=certifi.where())

        # context = ssl.create_default_context()
        # context.check_hostname = False
        # context.verify_mode = ssl.CERT_NONE

        video_links = []
        url = first_url
        while True:
            # ssl._create_default_https_context = ssl._create_unverified_context
            # context = ssl._create_unverified_context()
            # inp = urllib.request.urlopen(url, context=context)
            # resp = json.load(inp)

            response = requests.get(url, verify=certifi.where())

            # 检查响应状态码，如果请求成功，处理响应数据
            if response.status_code == 200:
                # 解析 JSON 响应
                resp = response.json()
            else:
                print(f'Error: Received status code {response.status_code}')

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except KeyError:
                break
        print(video_links)
        self.write_to_file(video_links, utils.get_video_list_filepath(channel_id))
        return video_links

    def write_to_file(self, video_link, filepath):
        with open(filepath, 'w') as f:
            for url in video_link:
                f.write(url + '\n')

    def read_file(self,filepath):
        video_links = []
        with open(filepath , 'r') as f:
            for url in f:
                video_links.append(url.strip())
        return video_links

