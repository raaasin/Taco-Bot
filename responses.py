import random
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
import sys
import os
import json

os.environ["OPENAI_API_KEY"]="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"


documents = SimpleDirectoryReader('tdata').load_data()
index = GPTVectorStoreIndex.from_documents(documents)
q=index.as_query_engine()

def handle_response(message) -> str:
    return q.query(message)

    