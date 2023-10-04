from abc import ABC, abstractmethod

class Iengine(ABC):
    @abstractmethod
    def need_service(self):
        pass