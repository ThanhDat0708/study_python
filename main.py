# Hệ thống RAG cơ bản với chromaDB và OPENAI API
# 1. Load tài liệu 'data-sample.txt'
# 2. Chunking tài liệu thành các đoạn nhỏ
# 3. Tạo embedding cho từng đoạn bằng openai_service.get_embedding
# 4. Thêm embedding vào ChromaDB
# 5. Nhận câu hỏi của người dùng, tìm kiếm 5 vector gần nhất trong ChromaDB
# 6. Gửi câu hỏi và các đoạn tìm đến OpenAi Responses API để nhận câu trả lời
# 7. Trả về câu trả lời cho người dùng và lập lại bước 5-7 cho các câu hỏi tiếp theo. Kết thúc khi người dùng nhạap văn bản rỗng

from loader import txt_loader
from chunker import chunk_by_token
from chromaDB_service import add_documents, search
from openai_service import get_response

COLLECTION_NAME = "noi_quy_abc"

content = txt_loader("data-sample.txt")
chunks = chunk_by_token(content)
ids = [f"chunk_{i}" for i in range(len(chunks))]
add_documents(COLLECTION_NAME, ids, chunks)

print("Đã nạp tài liệu vào ChromaDB. Hãy nhập câu hỏi (Enter trống để thoát).")

while True:
    query = input("\nCâu hỏi: ").strip()
    if not query:
        break
    results = search(COLLECTION_NAME, query, n_results=5)
    context = "\n\n".join(results["documents"][0])
    augmented_query = f"Dựa trên thông tin sau:\n{context}\n\nTrả lời câu hỏi: {query}"
    answer = get_response(augmented_query)
    print(f"Trả lời: {answer}")
