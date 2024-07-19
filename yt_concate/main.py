from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.get_video_list import GetvideoList
from yt_concate.pipeline.steps.step import StepException

CHANNEL_ID = 'UCTluGtOZneOOvmzMhvG7BYg'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }
    steps = [
        GetvideoList()
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()

