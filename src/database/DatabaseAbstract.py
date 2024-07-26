from typing import Protocol

class DatabaseAbstract(Protocol):

    def fetch_product_table(self, product_name: str):
        ...
    
    def disconnect(self):
        ...
    
