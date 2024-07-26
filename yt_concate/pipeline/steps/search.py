from yt_concate.pipeline.steps.step import Step


class Search(Step):
    def process(self, data, inputs, utils):
        word = inputs['search_word']
