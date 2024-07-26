from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.readcaption import Readcaption
from yt_concate.pipeline.steps.step import StepException
from yt_concate.utils import Utils

"""steps:
step1. get all video list from youtube
step2. download youtube subtitle
step3. download youtube
step4. edit video
"""

# CHANNEL_ID = 'UCTluGtOZneOOvmzMhvG7BYg'
CHANNEL_ID = 'UCQphRgAhj5UxktrQNP3WF5g'
# CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'incredible',
    }
    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
        Readcaption(),
        Postflight()
    ]

# 可用forloop去執行steps中的每一個step
    # for step in steps:
    #     try:
    #         step.process()
    #     except StepException as ex:
    #         print('catch', ex)
    #         break

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
