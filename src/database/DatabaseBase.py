from .DatabaseAbstract import DatabaseAbstract

class DatabaseBase(DatabaseAbstract):
    
    def __init__(self, config):
        self.config = config

    def fetch_product_table(self):
        pass
    
    def disconnect(self):
        pass
    