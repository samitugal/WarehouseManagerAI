from src.config_defs.database_config_defs import DatabaseMainConfig, DatabaseTag
from .DatabaseBase import DatabaseBase
from .Postgres import Postgres

class DatabaseManager:
    def __init__(self, config: MainConfig, database: DatabaseBaseClass):
        self.config = MainConfig
        self.database = database

    @staticmethod
    def new_instance_from_config(config: MainConfig):
        if config.db.database_tag == DatabaseTag.POSTGRESQL:
            return Postgres(config)
        else:
            raise NotImplementedError

    def fetch_product_table(self) -> :
        return self.database.fetch_product_table()

    def disconnect(self):
        self.database.disconnect()

if __name__ == "__main__":
    db = Database.new_instance_from_config(MainConfig)
    db.close()