import pinecone
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings

index = None

def init_pinecone():
    global index
    pinecone.init(api_key="your-key", environment="us-west1-gcp")
    if "legalgpt-index" not in pinecone.list_indexes():
        pinecone.create_index("legalgpt-index", dimension=1536)
    index = pinecone.Index("legalgpt-index")

def get_vector_store():
    return Pinecone(index, OpenAIEmbeddings().embed_query, "text")

def store_doc_embeddings(filename, content):
    text = content.decode("utf-8")
    docs = [{"text": text, "metadata": {"filename": filename}}]
    embedder = OpenAIEmbeddings()
    vectors = [{"id": filename, "values": embedder.embed_query(text), "metadata": {"filename": filename}}]
    index.upsert(vectors)
    return "stored"