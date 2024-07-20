from abc import ABC, abstractmethod


class Step(ABC):
    def __init__(self):
        pass

    @abstractmethod  # 這個代表子孫的class都一定要implement這方法
    def process(self, data, inputs):  # 這是一個interface(介面)
        pass


class StepException(Exception):
    pass
