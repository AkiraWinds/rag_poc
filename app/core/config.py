'''
language models configuration for embedding and text generation
Import this module to access the configured models.
'''


import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
load_dotenv()

slm_embedding = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=os.getenv("SLM_API_KEY")
)

slm_generation = OpenAIEmbeddings(
    model="gpt-5-mini",
    api_key=os.getenv("SLM_API_KEY")
)
