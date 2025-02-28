'''
Author : Karan Chauhan
Github : Karan-Chauhan19
Organization : L.J University
'''
from langchain_community.llms import HuggingFaceHub
import os
from dotenv import load_dotenv
load_dotenv()




os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")

hf = HuggingFaceHub(
    repo_id="mistralai/Mistral-7B-v0.1",
    model_kwargs={"temperature":0.1,"max_length":500}
)