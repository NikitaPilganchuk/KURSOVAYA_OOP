from abc import ABC, abstractmethod

class JsonSaver(ABC):

    @abstractmethod
    def save(self):
        pass
