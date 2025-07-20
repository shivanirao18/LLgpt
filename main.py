from fastapi import FastAPI, UploadFile, File
from chains import get_chat_response
from vectorstore import init_pinecone, store_doc_embeddings

app = FastAPI()

@app.on_event("startup")
def startup():
    init_pinecone()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    result = store_doc_embeddings(file.filename, content)
    return {"status": result}

@app.post("/chat")
async def chat(user_input: str):
    response = get_chat_response(user_input)
    return {"response": response}