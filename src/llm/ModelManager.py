from typing import List, Dict, Any

from src.config_defs.llm_config_defs import LLMTag, LLMMainConfig
from .ModelBase import ModelBase

class ModelManager:
    def __init__(self, config: LLMMainConfig, llm: ModelBase):
        self.config = config
        self.llm = llm

    @staticmethod
    def new_instance_from_config(config: LLMMainConfig) -> "ModelManager": 
        from .BedrockModel import Bedrock
        from .OpenAIModel import OpenAI

        match config.llm.llm_tag:
            case LLMTag.BEDROCK:
                return ModelManager(config, Bedrock(config))
            case LLMTag.OPENAI:
                return ModelManager(config, OpenAI(config))
            case _:
                raise ValueError("Invalid LLM tag")

    def provide_information(self, user_request: str, chat_history: List[Dict[str, Any]] = []) -> str:
        return self.llm.provide_information(user_request)
