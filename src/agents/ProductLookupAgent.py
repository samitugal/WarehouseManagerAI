import os
from typing import List, Dict, Any
from dotenv import load_dotenv

from langchain import hub
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain_core.tools import Tool
from langchain.prompts.prompt import PromptTemplate
from langchain.chat_models import init_chat_model

from src.tools.ProductTools import get_product_information_from_embeddings, get_product_information_from_db
from src.utils.PromptLoader import load_prompt
from src.config_defs.llm_config_defs import LLMMainConfig, LLMTag

load_dotenv()

class ProductLookupAgent:
    def __init__(self):
        self.llm = self._initialize_llm()
        self.prompt_template = self._load_prompt_template()
        self.agent_executor = self._create_agent_executor()

    def _initialize_llm(self):
        cfg = LLMMainConfig.from_file(os.getenv("LLM_CONFIG_PATH"))
        
        if cfg.llm.llm_tag == LLMTag.BEDROCK:
            return init_chat_model(
                cfg.bedrock.model_id, 
                model_provider=cfg.bedrock.model_provider, 
                region_name=cfg.bedrock.region_name
            )
        elif cfg.llm.llm_tag == LLMTag.OPENAI:
            return init_chat_model(
                cfg.openai.model_name, 
                model_provider=cfg.openai.model_provider, 
                temperature=cfg.llm.temperature
            )
        else:
            raise ValueError("Invalid LLM tag")

    def _load_prompt_template(self):
        template = load_prompt("agent_prompt_template")
        return PromptTemplate(
            template=template, input_variables=["input", "chat_history"]
        )

    def _create_agent_executor(self):
        tools_for_agent = [
            Tool(
                name="Searche for information about product in embeddings.",
                func=get_product_information_from_embeddings,
                description="""
                    Searches for information about embeddings and provides information or description which helps general information
                    about product origin, ingredients, etc..
                    """,
            ),
            Tool(
                name="Search Product database to get information like product_id, product_name, supplier_name, category_name, quantity_per_unit, unit_price, units_in_stock, units_on_order, reorder_level, discontinued",
                func=get_product_information_from_db,
                description="""
                Useful for when you need to get information about a product in inventory. Information like product_id, product_name, 
                supplier_name, category_name, quantity_per_unit, unit price, units in stock, units on order, reorder level, and discontinued status.
                => To use this function, only pass the product name as a string.
                """,
            )
        ]
        react_prompt = hub.pull("hwchase17/react")
        agent = create_react_agent(llm=self.llm, tools=tools_for_agent, prompt=react_prompt)
        return AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    def lookup(self, query: str, chat_history: List[Dict[str, Any]] = []) -> str:
        try:
            formatted_input = self.prompt_template.format_prompt(input=query, chat_history=chat_history)
            result = self.agent_executor.invoke(input={"input": formatted_input})
            return result["output"]
        except Exception as e:
            return "Agent has no idea"

