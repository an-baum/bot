import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

def search_documents(query, documents):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_vec = model.encode(query)
    embeddings = [doc['embedding'] for doc in documents.values()]
    texts = [doc['text'] for doc in documents.values()]
    
    index = faiss.IndexFlatL2(len(query_vec))
    index.add(np.array(embeddings))
    
    _, I = index.search(np.array([query_vec]), k=1)
    return texts[I[0][0]]
