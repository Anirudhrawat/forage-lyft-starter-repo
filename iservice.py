from abc import ABC, abstractmethod

class Iservice(ABC):
    @abstractmethod
    def needs_service(self):
        pass