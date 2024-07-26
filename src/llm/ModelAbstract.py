from abc import ABC, abstractmethod
from typing import List, Dict, Any

class ModelAbstract(ABC):

    @abstractmethod
    def provide_information(self, user_request: str, chat_history: List[Dict[str, Any]] = []) -> str:
        pass

    