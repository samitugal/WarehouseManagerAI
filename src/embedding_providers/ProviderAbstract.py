from abc import ABC, abstractmethod
from typing import List


class ProviderAbstract(ABC):

    @abstractmethod
    def ingest_docs(self):
        pass
    
    @abstractmethod
    def search_embeddings(self, query: str):
        pass