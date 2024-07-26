from typing import List, Dict, Any

from src.config_defs.llm_config_defs import LLMTag, LLMMainConfig
from .ModelBase import ModelBase

class Pipeline:
    def __init__(self, config: LLMMainConfig, llm: ModelBase):
        self.config = config
        self.llm = llm

    @staticmethod
    def new_instance_from_config(config: LLMMainConfig) -> "Pipeline": 
        from .BedrockModel import Bedrock
        from .OpenAIModel import OpenAI

        match config.llm.llm_tag:
            case LLMTag.BEDROCK:
                return Pipeline(config, Bedrock(config))
            case LLMTag.OPENAI:
                return Pipeline(config, OpenAI(config))
            case _:
                raise ValueError("Invalid LLM tag")

    def provide_information(self, user_request: str) -> str:
        return self.llm.provide_information(user_request)

if __name__ == "__main__":
    cfg = LLMMainConfig.from_file("/home/user/inventoryqabot/configs/LLM/openai.yaml")
    history_llm = Pipeline.new_instance_from_config(config = cfg)

    user_request = "What is chai"
    response = history_llm.provide_information(user_request)
    print(response)

    user_request = "What is the category code of it."
    response = history_llm.provide_information(user_request)
    print(response)
