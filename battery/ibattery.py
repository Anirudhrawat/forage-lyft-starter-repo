from abc import ABC, abstractmethod

class Ibattery(ABC):
    @abstractmethod
    def need_service(self):
        pass