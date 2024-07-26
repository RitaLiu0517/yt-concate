from yt_concate.pipeline.steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs, utils):
        data = None  # 因是一個步驟結束丟到下個步驟繼續加工，所以第二步驟開始會多了參數data
        for step in self.steps:
            try:
                data = step.process(data, inputs, utils)
            except StepException as ex:
                print('Catch Exception:', ex)
                break
