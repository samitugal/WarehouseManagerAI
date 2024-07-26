import os

from dotenv import load_dotenv

from src.embedding_providers.EmbeddingsPipeline import EmbeddingsPipeline
from src.config_defs.embeddings_config_defs import EmbeddingsMainConfig

load_dotenv()

def get_product_information_from_embeddings(query: str):
    """
        Searches for information about embeddings and provides information about product in inventory
    """
    cfg = EmbeddingsMainConfig.from_file(os.getenv('EMBEDDINGS_CONFIG_PATH'))
    embedding_instance = EmbeddingsPipeline.new_instance_from_config(config= cfg)
    result = embedding_instance.search_embeddings(query)
    return result
