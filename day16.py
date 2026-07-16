import fitz
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        text += page.get_text()

    return text



def clean_text(text):
    text = text.replace("\n", " ")
    text = " ".join(text.split())
    return text



def chunk_text(text, chunk_size=400):

    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i+chunk_size]))

    return chunks




model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embeddings(chunks):

    embeddings = model.encode(chunks)

    return np.array(embeddings).astype("float32")



def build_index(embeddings):

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index



def search(query, index, chunks):

    query_vector = model.encode([query]).astype("float32")

    distance, ids = index.search(query_vector, k=3)

    print("\nMost Relevant Results\n")

    for i in ids[0]:
        print("----------------------------------")
        print(chunks[i])
        print()



pdf = input("Enter PDF filename: ")

text = extract_text(pdf)

text = clean_text(text)

chunks = chunk_text(text)

embeddings = create_embeddings(chunks)

index = build_index(embeddings)

while True:

    q = input("\nAsk Question (or exit): ")

    if q.lower() == "exit":
        break

    search(q, index, chunks)
