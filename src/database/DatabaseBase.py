from .DatabaseAbstract import DatabaseAbstract

class DatabaseBase(DatabaseAbstract):
    
    def __init__(self, config):
        self.config = config

    def fetch_product_table(self, product_name: str):
        pass
    
    def disconnect(self):
        pass
    