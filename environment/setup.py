'''
author : Karan Chauhan
github : @Karan-Chauhan19
organization : L.J University
'''

from setuptools import  setup, find_packages

setup(
    name='Healthcare Chatbot',  # project name
    version='1.0',  # version number
    description="This project involves developing an AI-powered Healthcare Chatbot using a Retrieval-Augmented Generation (RAG) pipeline. The chatbot will assist users in answering medical-related queries, providing health information, and suggesting possible courses of action based on reliable sources. The RAG pipeline ensures accurate and up-to-date responses by retrieving relevant information from a knowledge base before generating responses.",  # description of the project
    packages = find_packages(),  # find all packages
    author='Karan-Chauhan' ,# author of the package
    author_email='kc879022@gmail.com', # email of the author
    url='https://github.com/Karan-Chauhan19/Healthcare-Chatbot', # url of the project
    install_requires=['langchain', 'langchain_community', 'chromadb', 'sentence-transformers','pypdf','python-dotenv','streamlit'],
    # list of the dependencies required by the package
    classifiers=['Programming Language :: python :: 3.12.3']
)