import string
from typing import TypeVar, List, Dict, Any
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from collections import deque  # Import deque for history management

from .ModelAbstract import ModelAbstract
from src.utils.PromptLoader import load_prompt
from src.agents.ProductLookupAgent import ProductLookupAgent

U = TypeVar("U", bound=BaseModel)

class ModelBase(ModelAbstract):
    def __init__(self, config, history_length: int = 5):
        self.config = config
        load_dotenv()
        self.history = deque(maxlen=history_length)
    
    def _create_chain(self, template: str, input_variables: List[str], partial_variables: Dict[str, Any], parser = None, model_info: str = None):
        prompt_template = PromptTemplate(
            input_variables=input_variables, 
            template=template, 
            partial_variables=partial_variables
        )
        if model_info:
            self.client.model_kwargs["messages"] = [{"model_info": model_info}]
        
        if parser:
            return prompt_template | parser | self.client
        else:
            return prompt_template | self.client

    def provide_information(self, user_request: str, chat_history: List[Dict[str, Any]] = []) -> str:
        prompt_template = load_prompt("information_provider_template")

        agent = ProductLookupAgent()
        
        search_info = agent.lookup(user_request)

        chain = self._create_chain(prompt_template, ["chat_history", "local_search_information", "user_request"], {})

        response = chain.invoke(input={"chat_history": chat_history, "local_search_information": search_info, "user_request": user_request})

        return response
