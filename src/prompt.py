from langchain.prompts import PromptTemplate

prompt_template = """
You are a healthcare chatbot providing clear and medically accurate responses.

**User’s Question:** {question}

**Medical Information:**
{context}

**Your Response:**
"""

prompt = PromptTemplate(template=prompt_template,input_variables=["context","question"])