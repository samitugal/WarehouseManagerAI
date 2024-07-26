import warnings

from langchain_openai import ChatOpenAI

from .ModelBase import ModelBase
from src.config_defs.llm_config_defs import LLMTag, LLMMainConfig

warnings.filterwarnings("ignore", category=DeprecationWarning, module='langchain')

class Bedrock(ModelBase):
    def __init__(self, config):
        super().__init__(config)
        if config.llm.llm_tag != LLMTag.BEDROCK:
            raise ValueError("BedrockPipeline can only be used with Bedrock")
        if config.bedrock is None:
            raise ValueError("BedrockPipeline requires a BedrockConfig")

        bedrock = boto3.client(service_name='bedrock-runtime', region_name=config.bedrock.region_name)
        self.client = BedrockChat(model_id=config.bedrock.model_id, client=bedrock, model_kwargs={"temperature": config.llm.temperature})
