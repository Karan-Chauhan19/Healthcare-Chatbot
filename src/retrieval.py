from helper import Helper
import model
from langchain.chains import RetrievalQA
import prompt

db = Helper().get_or_create_embeddings()

retriever = db.as_retriever(search_type="similarity",search_kwargs={"k":1})

retrievalQA = RetrievalQA.from_chain_type(
    llm=model.hf,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt":prompt.prompt}
)