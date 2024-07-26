import os

def load_prompt(template_name: str):
    """
        Load a prompt template from the prompts directory.
    """
    template_path = os.path.join(os.path.dirname(__file__), '..', 'prompts', f"{template_name}.txt")
    with open(template_path, 'r') as file:
        return file.read()

def fill_prompt(template, **kwargs):
    return template.format(**kwargs)