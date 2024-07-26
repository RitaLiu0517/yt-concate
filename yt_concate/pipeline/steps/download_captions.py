import yt_dlp
from pytube import YouTube
from yt_concate.pipeline.steps.step import Step


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        for url in data:
            if utils.caption_file_exist(url):
                print('caption exist:continue')
                continue

            source = YouTube(url)
            available_captions = source.captions
            # en_caption = source.captions['a.en']
            if not available_captions:
                print("No captions available for this video.")
                return

            print("Available captions:", available_captions)

            try:
                en_caption = source.captions.get_by_language_code('en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
                print(en_caption_convert_to_srt)
            except AttributeError as ex:
                print('catch ex', ex)
                continue

            text_file = open(utils.get_caption_filepath(url), "w")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
            break

            # # 設置下載選項
            # ydl_opts = {
            #     'writesubtitles': True,
            #     'subtitleslangs': ['en', 'zh-Hans'],  # 指定多個字幕語言
            #     'format': 'best',  # 下載最佳質量視頻
            #     'outtmpl': '%(title)s.%(ext)s',  # 文件保存格式
            # }
            #
            # # 下載視頻和字幕
            # with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            #     ydl.download([url])
            #     break
            #
            #

            # ydl_opts = {
            #     'writesubtitles': True,
            #     'subtitleslangs': ['en', 'zh-Hans'],  # 指定多個字幕語言
            #     'format': 'best',  # 下載最佳質量視頻
            #     'outtmpl': f'{download_dir}/%(title)s.%(ext)s',  # 文件保存格式，指定目錄
            # }

            # # 下載視頻和字幕
            # with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            #     result = ydl.extract_info(url, download=True)
            #
            # # 獲取視頻標題
            # video_title = result.get('title', 'unknown_title').replace('/', '_')
            #
            # # 獲取下載的字幕文件路徑
            # subtitles_info = result.get('requested_subtitles')
            # if subtitles_info:
            #     for lang, subtitle in subtitles_info.items():
            #         subtitle_path = subtitle['filepath']
            #         print(f"Subtitles ({lang}) for {video_title}:")
            #
            #         # 讀取字幕內容
            #         with open(subtitle_path, 'r', encoding='utf-8') as file:
            #             subtitle_content = file.read()
            #             print(subtitle_content)
            #
            #         # 將字幕內容保存到單獨的txt文件
            #         subtitle_txt_path = os.path.join(subtitles_dir, f"{video_title}_{lang}.txt")
            #         with open(subtitle_txt_path, 'w', encoding='utf-8') as file:
            #             file.write(subtitle_content)
            # break


