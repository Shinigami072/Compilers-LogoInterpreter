from abc import ABC

from interpreter.runtime.Model import Environment


class EnvironmentDisplay(ABC):
    def __init__(self, environment: Environment):
        self.environment = environment

    def close(self):
        pass
