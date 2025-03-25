'''
author : Karan Chauhan
github : Karan-Chauhan19
organization : L.J University
'''

import os
import re
import streamlit as st
from retrieval import retrievalQA

def clean_chatbot_response(response):
    # Define a pattern to match everything before the structured response
    pattern = r"You are a healthcare chatbot.*?\*\*Your Response:\*\*"

    # Remove the unwanted part (chatbot prompt and metadata)
    cleaned_response = re.sub(pattern, "", response, flags=re.DOTALL).strip()

    return cleaned_response


st.title("HealthCare Chatbot")
message = st.text_input("Message Chatbot")

if message :
    result = retrievalQA.invoke(message)
    cleaned_response = clean_chatbot_response(result['result'])
    st.write(cleaned_response)
