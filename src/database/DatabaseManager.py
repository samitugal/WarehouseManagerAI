from src.config_defs.database_config_defs import DatabaseMainConfig, DatabaseTag
from .DatabaseBase import DatabaseBase
from .Postgres import Postgres

class DatabaseManager:
    def __init__(self, config: DatabaseMainConfig, database: DatabaseBase):
        self.config = config
        self.database = database

    @staticmethod
    def new_instance_from_config(config: DatabaseMainConfig):
        if config.db.database_tag == DatabaseTag.POSTGRESQL:
            return Postgres(config)
        else:
            raise NotImplementedError

    def fetch_product_table(self, product_name: str):
        return self.database.fetch_product_table(product_name)

    def disconnect(self):
        self.database.disconnect()

if __name__ == "__main__":
    cfg = DatabaseMainConfig.from_file("configs\Database\postgresql.yaml")
    db_manager = DatabaseManager.new_instance_from_config(cfg)
    products = db_manager.fetch_product_table("Chai")