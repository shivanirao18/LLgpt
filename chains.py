from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from vectorstore import get_vector_store

qa = None

def get_chat_response(query):
    global qa
    if not qa:
        qa = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(temperature=0),
            retriever=get_vector_store().as_retriever()
        )
    return qa.run(query)