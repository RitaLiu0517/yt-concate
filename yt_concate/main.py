from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.step import StepException

"""steps:
step1. get all video list from youtube
step2. download youtube subtitle
step3. download youtube
step4. edit video
"""

CHANNEL_ID = 'UCTluGtOZneOOvmzMhvG7BYg'


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
    }
    steps = [
        GetVideoList(),
    ]

# 可用forloop去執行steps中的每一個step
    # for step in steps:
    #     try:
    #         step.process()
    #     except StepException as ex:
    #         print('catch', ex)
    #         break

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
