A document-aware legal chatbot built with FastAPI, LangChain, and Pinecone.
Features:
- Upload legal documents (TXT, PDF)
- Chat with GPT about uploaded content
- Context-aware answers using vector similarity (Pinecone)
- Modular, scalable backend with FastAPI
Tech Stack:
- LangChain
- OpenAI API
- Pinecone
- FastAPI
Setup:
1.Install dependencies
pip install -r requirements.txt
2.Create ".env"
```env
OPENAI_API_KEY=your-openai-api-key
PINECONE_API_KEY=your-pinecone-api-key
PINECONE_ENV=your-pinecone-environment
```
3.Run app
```bash
uvicorn main:app --reload
```
Endpoints:
- `POST /upload`: Upload a document
- `POST /chat`: Chat with GPT using stored context
TODO:
- Add UI with Streamlit
- Add user accounts
