import chromadb
from rag_terminal.openai_service import get_embedding

db = chromadb.EphemeralClient()

def create_collection(name: str):
    return db.get_or_create_collection(name=name)

def get_collection(name: str):
    return db.get_collection(name=name)

def list_collections():
    return db.list_collections()

def delete_collection(name: str):
    db.delete_collection(name=name)

def add_documents(collection_name: str, ids: list[str], documents: list[str], metadatas: list[dict] | None = None):
    collection = db.get_or_create_collection(name=collection_name)
    embeddings = get_embedding(documents)
    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=documents,
        metadatas=metadatas
    )

def search(collection_name: str, query: str, n_results: int = 5):
    collection = db.get_or_create_collection(name=collection_name)
    query_embedding = get_embedding([query])[0]
    return collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
