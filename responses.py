import random
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
import sys
import os
import json
import creds
'''
os.environ["OPENAI_API_KEY"]=creds.open


documents = SimpleDirectoryReader('tdata').load_data()
index = GPTVectorStoreIndex.from_documents(documents)
q=index.as_query_engine()

def handle_response(message) -> str:
    return q.query(message)

'''