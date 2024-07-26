from yt_concate.model.yt import YT
from yt_concate.pipeline.steps.step import Step


class InitializeYT(Step):
    def process(self, data, inputs, utils):
        return [YT(url) for url in data]
