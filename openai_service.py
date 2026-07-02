#  tạo embedding bằng text-embedding-3-small
#  Gửi request đến API của OpenAI chat gpt-5.4-mini
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

# System prompt ngan gon
SYSTEM_PROMPT = """Bạn là một trợ lý AI thông minh,hữu ích và thân thiện. 
 Hãy trả lời các câu hỏi một cách ngắn gọn, rõ ràng và chính xác.
 Chat theo ngữ cảnh của câu hỏi không trả lời ngoài pham vi câu hỏi. 
 Nếu không biết câu trả lời,hãy trả lời"Câu hỏi không thuộc phạm vi kiến thức của tôi."."""
# lich su hoi thoai
chat_history = []

def get_embedding(text: list[str])->list[list[float]]:
    """
    Tạo embedding cho văn bản bằng mô hình text-embedding-2-small.

    Args:
        text (str): Văn bản cần tạo embedding.
        model (str): Tên mô hình để tạo embedding.

    Returns:
        List[float]: Danh sách các giá trị embedding.
    """
    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )
    return [item.embedding for item in response.data]

def get_response(user_message: str)-> str:
    """
    Gửi yêu cầu đến API của OpenAI để nhận phản hồi từ mô hình chat.

    Args:
        user_message (str): Tin nhắn của người dùng.

    Returns:
        str: Phản hồi từ mô hình chat.
    """
    # Thêm tin nhắn của người dùng vào lịch sử hội thoại
    chat_history.append({"role": "user", "content": user_message})

    # Gửi yêu cầu đến API của OpenAI
    try:
        response = client.chat.completions.create(
            model="gpt-5.4-mini",
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + chat_history,
            max_completion_tokens=150,
            temperature=0.7
        )
    except Exception as e:
        print(f"Error occurred: {e}")
        return "Xin lỗi, đã xảy ra lỗi khi xử lý yêu cầu của bạn."


    # Lấy phản hồi từ mô hình
    assistant_message = response.choices[0].message.content

    # Thêm phản hồi của trợ lý vào lịch sử hội thoại
    chat_history.append({"role": "assistant", "content": assistant_message})

    return assistant_message