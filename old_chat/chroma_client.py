import chromadb

# tao database neu chua co
db = chromadb.PersistentClient(
    path="./chroma_db"
    )


# tạo hoặc truy xuất đến 1 bảng
tbl_tai_lieu = db.get_or_create_collection(
    name="tai_lieu"
)
    

ids = ["doc_1", "doc_2", "doc_3", "doc_4", "doc_5"]
documents = [
    "Vocabulary refers to the body of words used in a particular language.",
    "Pronunciation is the way in which a word or a language is spoken.",
    "Listening comprehension is the ability to understand spoken language.",
    "Spaced repetition is a highly effective learning technique for memorizing new words.",
    "A bilingual dictionary translates words from one language to another."
]
metadatas = [
    {"category": "concept", "difficulty": "beginner"},
    {"category": "skill", "difficulty": "intermediate"},
    {"category": "skill", "difficulty": "intermediate"},
    {"category": "methodology", "difficulty": "advanced"},
    {"category": "tool", "difficulty": "beginner"}
]


#  chuyển documents thành vector bằng text-embedding-3-small
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

response = client.embeddings.create(
    input= documents,
    model="text-embedding-3-small"
)

embeddings = [x.embedding for x in response.data]

# thêm vào database, bằng tai liệu
tbl_tai_lieu.add(
    ids=ids,
    embeddings=embeddings,
    documents=documents,
    metadatas=metadatas

)
user_input = input("Nhập nội dung vào:")
response = client.embeddings.create(
    input= user_input,
    model="text-embedding-3-small"
)
user_input_vector = response.data[0].embedding
# tim kiem
res = tbl_tai_lieu.query(
    query_embeddings=[user_input_vector],
    n_results=3
)
print("kết quả tìm kiếm:")
print("Khoảng cách: ",res["distances"])
print("Tài liệu:",res["documents"])