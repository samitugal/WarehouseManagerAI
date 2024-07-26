from typing import Protocol

class DatabaseAbstract(Protocol):

    def fetch_product_table(self):
        ...
    
    def disconnect(self):
        ...
    
