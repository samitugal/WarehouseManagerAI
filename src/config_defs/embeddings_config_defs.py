from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
import omegaconf
from omegaconf import OmegaConf

class EmbeddingsTag(Enum):
    PINECONE = "pinecone"

class EmbeddingsType(Enum):
    OPENAI = "openai"

@dataclass
class EmbeddingsConfig:
    provider_tag: EmbeddingsTag = omegaconf.MISSING
    embeddings_type: EmbeddingsType = omegaconf.MISSING

@dataclass
class PineconeConfig:
    index_name: str = omegaconf.MISSING

@dataclass
class OpenAIConfig:
    embeddings_model_name: str = omegaconf.MISSING

@dataclass
class EmbeddingsMainConfig:
    provider: EmbeddingsConfig = field(default_factory=EmbeddingsConfig)
    pinecone: Optional[PineconeConfig] = None
    openai: Optional[OpenAIConfig] = None

    @staticmethod
    def from_file(yaml_path: str) -> "EmbeddingsMainConfig":
        conf = OmegaConf.structured(EmbeddingsMainConfig)
        conf = OmegaConf.merge(conf, OmegaConf.load(yaml_path))
        return conf

if __name__ == "__main__":
    cfg = EmbeddingsMainConfig()
    yaml_str = OmegaConf.to_yaml(cfg)

    conf = OmegaConf.structured(EmbeddingsMainConfig)
    conf = OmegaConf.merge(conf, OmegaConf.load("/home/user/inventoryqabot/configs/Embeddings/pinecone.yaml"))
    print(conf)
