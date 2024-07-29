import os

from langchain import hub
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from dotenv import load_dotenv

from src.tools.ProductTools import get_product_information_from_embeddings, get_product_information_from_db

load_dotenv()

class ProductLookupAgent:
    def __init__(self):
        llm = ChatOpenAI(
            temperature=0
        )
        template = """
        You are a helpful assistant that provides information about products in inventory.
        User wants to know information about {input}. Please answer questions about the product.
        """
        self.prompt_template = PromptTemplate(
            template=template, input_variables=["input"]
        )
        tools_for_agent = [
            Tool(
                name="Search Product embeddings to get information",
                func=get_product_information_from_embeddings,
                description="useful for when you need get the information about Product in inventory. Information like description",
            ),
            Tool(
                name="Search Product database to get information like product_id, product_name, supplier_name, category_name, quantity_per_unit, unit_price, units_in_stock, units_on_order, reorder_level, discontinued",
                func=get_product_information_from_db,
                description="""
                useful for when you need get the information about Product in inventory. Information like product_id, product_name, 
                supplier_name, category_name, quantity_per_unit, unit_price, units_in_stock, units_on_order, reorder_level, discontinued
                => To use this function, only pass the product name as a string.
                """,
            )
        ]
        react_prompt = hub.pull("hwchase17/react")
        self.agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
        self.agent_executor = AgentExecutor(agent=self.agent, tools=tools_for_agent, verbose=True)

    def lookup(self, query: str) -> str:
        try:
            result = self.agent_executor.invoke(
                input={"input": self.prompt_template.format_prompt(input=query)}
            )

            result = result["output"]
            return result
        except Exception as e:
            return "Agent has no idea"
