# -*- coding: utf-8 -*-
"""CHATBOT

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OM-9bkfzMZEERlai4yvW7Tv47xApARL1
"""

! git clone https://github.com/uttero/stillpress-substack.git

! pip install gpt-index
! pip install langchain

from gpt_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import sys
import os
from IPython.display import Markdown, display

def construct_index(directory_path):
    # set maximum input size
    max_input_size = 4096
    # set number of output tokens
    num_outputs = 256
    # set maximum chunk overlap
    max_chunk_overlap = 20
    # set chunk size limit
    chunk_size_limit = 600

    # define LLM
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-003", max_tokens=num_outputs))
    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
 
    documents = SimpleDirectoryReader(directory_path).load_data()
    
    index = GPTSimpleVectorIndex(
        documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper
    )

    index.save_to_disk('index.json')

    return index

def ask_paul():
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    while True: 
        query = input("What do you want to ask Paul?")
        response = index.query(query, response_mode="compact")
        display(Markdown(f"Paul Bot says: <b>{response.response}</b>"))

os.environ["OPENAI_API_KEY"] = input("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")

pip install PyPDF2

construct_index('/content/stillpress-substack')

ask_paul()