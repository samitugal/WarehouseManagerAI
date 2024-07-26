from src.config_defs.embeddings_config_defs import EmbeddingsMainConfig, EmbeddingsTag
from .ProviderBase import ProviderBase

class EmbeddingsPipeline:
    def __init__(self, config: EmbeddingsMainConfig, embeddings: ProviderBase):
        self.config = config
        self.embeddings = embeddings

    @staticmethod
    def new_instance_from_config(config: EmbeddingsMainConfig) -> "EmbeddingsPipeline": 
        from .Pinecone import Pinecone

        match config.provider.provider_tag:
            case EmbeddingsTag.Pinecone:
                return Pipeline(config, Pinecone(config))
            case _:
                raise ValueError("Invalid Embeddings tag")

    def ingest_docs(self):
        return self.embeddings.ingest_docs()
