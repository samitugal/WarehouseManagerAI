from .ProviderAbstract import ProviderAbstract

class ProviderBase(ProviderAbstract):
    
    def __init__(self, config):
        self.config = config

    def ingest_docs(self):
        pass
    
    def search_embeddings(self, query: str):
        pass