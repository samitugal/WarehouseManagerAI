import inspect
import string

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
            input = input[len(prefix):]

        # Only remove potentially harmful characters, not all punctuation
        harmful_chars = ";--'\"\n"
        translator = str.maketrans('', '', harmful_chars)
        cleaned_input = input.translate(translator).strip()
        return cleaned_input
