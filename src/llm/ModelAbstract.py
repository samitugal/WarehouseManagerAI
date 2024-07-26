from abc import ABC, abstractmethod

class ModelAbstract(ABC):

    @abstractmethod
    def provide_information(self, user_request: str) -> str:
        pass

    