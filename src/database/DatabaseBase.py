import inspect

from .DatabaseAbstract import DatabaseAbstract

class DatabaseBase(DatabaseAbstract):
    
    def __init__(self, config):
        self.config = config

    def fetch_product_table(self, product_name: str):
        pass
    
    def disconnect(self):
        pass

    def clean_input_from_agent(self, method: callable, input: str) -> str:
        method_signature = inspect.signature(method)
        param_name = next(iter(method_signature.parameters))
        
        prefix = f"{param_name}="
        if input.startswith(prefix):
            value_with_quotes = input[len(prefix):]
            
            if value_with_quotes.startswith('"') and value_with_quotes.endswith('"'):
                return value_with_quotes[1:-1]
            elif value_with_quotes.startswith("'") and value_with_quotes.endswith("'"):
                return value_with_quotes[1:-1]

        return input
    