import os
from dotenv import load_dotenv
from typing import List

from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

from src.config_defs.embeddings_config_defs import EmbeddingsType, EmbeddingsTag, EmbeddingsMainConfig
from .ProviderBase import ProviderBase

load_dotenv()

class Pinecone(ProviderBase):
    def __init__(self, config):
        super().__init__(config)
        self.index_name = config.pinecone.index_name
        self.embeddings = None

        if(config.provider.provider_tag == EmbeddingsTag.PINECONE):
            if(config.provider.embeddings_type == EmbeddingsType.OPENAI):
                self.embeddings = OpenAIEmbeddings(model=config.openai.embeddings_model_name)
            

    def load_documents_from_directory(self, directory):
        documents = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".txt"):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        doc = Document(page_content=content, metadata={"source": file_path})
                        documents.append(doc)
        return documents

    def ingest_docs(self):
        raw_documents = self.load_documents_from_directory("/home/user/inventoryqabot/data")
        print(f"loaded {len(raw_documents)} documents")

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
        documents = text_splitter.split_documents(raw_documents)

        print(f"Going to add {len(documents)} to Pinecone")
        PineconeVectorStore.from_documents(documents, self.embeddings, index_name=self.index_name)
        print("****Loading to vectorstore done ***")
    
    def search_embeddings(self, query: str):
        docsearch = PineconeVectorStore(index_name=self.index_name, embedding=self.embeddings)
        result = docsearch.search(query, search_type="similarity")
        return result


if __name__ == "__main__":
    config = EmbeddingsMainConfig.from_file("configs\Embeddings\pinecone.yaml")
    pinecone = Pinecone(config)
    print(pinecone.search_embeddings("What is Chef Anton's Cajun Seasoning"))
