from yt_concate.pipeline.steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs):
        data = None
        for step in self.steps:
            try:
                step.process(data, inputs)
            except StepException as ex:
                print('Catch Exception:', ex)
                break
