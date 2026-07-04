import chromadb
from openai_service import get_embedding

db = chromadb.PersistentClient(path="./chroma_db")

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

def get_all_documents(collection_name: str):
    collection = db.get_or_create_collection(name=collection_name)
    return collection.get()

def get_sources(collection_name: str):
    collection = db.get_or_create_collection(name=collection_name)
    all_data = collection.get()
    if not all_data or not all_data.get("metadatas"):
        return set()
    sources = set()
    for m in all_data["metadatas"]:
        if m and "source" in m:
            sources.add(m["source"])
    return sources

def delete_documents_by_ids(collection_name: str, ids: list[str]):
    collection = db.get_or_create_collection(name=collection_name)
    collection.delete(ids=ids)

def delete_documents_by_source(collection_name: str, source: str):
    collection = db.get_or_create_collection(name=collection_name)
    all_data = collection.get()
    if not all_data or not all_data.get("ids"):
        return
    ids_to_delete = []
    for i, doc_id in enumerate(all_data["ids"]):
        meta = all_data["metadatas"][i] if all_data.get("metadatas") else {}
        if meta and meta.get("source") == source:
            ids_to_delete.append(doc_id)
    if ids_to_delete:
        collection.delete(ids=ids_to_delete)
