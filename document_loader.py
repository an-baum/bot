import os
from sentence_transformers import SentenceTransformer

def load_documents():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    documents = {}
    for filename in os.listdir('data'):
        if filename.endswith('.txt') or filename.endswith('.md'):
            with open(os.path.join('data', filename), 'r', encoding='utf-8') as file:
                text = file.read()
                embedding = model.encode(text)
                documents[filename] = {'text': text, 'embedding': embedding}
    return documents
