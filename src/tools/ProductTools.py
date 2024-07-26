import os

from dotenv import load_dotenv

from src.embedding_providers.EmbeddingsPipeline import EmbeddingsPipeline
from src.config_defs.embeddings_config_defs import EmbeddingsMainConfig

from src.database.DatabaseManager import DatabaseManager
from src.config_defs.database_config_defs import DatabaseMainConfig

load_dotenv()

def get_product_information_from_embeddings(query: str):
    """
        Searches for information about embeddings and provides information about product in inventory
    """
    cfg = EmbeddingsMainConfig.from_file(os.getenv('EMBEDDINGS_CONFIG_PATH'))
    embedding_instance = EmbeddingsPipeline.new_instance_from_config(config= cfg)
    result = embedding_instance.search_embeddings(query)
    return result

def get_product_information_from_db(product_name: str):
    """
        Provides information about product in database. Information like     
        product_id: int
        product_name: str
        supplier_name: str
        category_name: str
        quantity_per_unit: str
        unit_price: float
        units_in_stock: int
        units_on_order: int
        reorder_level: int
        discontinued: bool
    """
    cfg = DatabaseMainConfig.from_file(os.getenv('DATABASE_CONFIG_PATH'))
    db_instance = DatabaseManager.new_instance_from_config(config= cfg)
    result = db_instance.fetch_product_table(product_name)
    return result

