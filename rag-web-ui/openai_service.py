from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

SYSTEM_PROMPT = """Bạn là một trợ lý AI thông minh,hữu ích và thân thiện. 
 Hãy trả lời các câu hỏi một cách ngắn gọn, rõ ràng và chính xác.
 Chat theo ngữ cảnh của câu hỏi không trả lời ngoài pham vi câu hỏi. 
 Nếu không biết câu trả lời,hãy trả lời"Câu hỏi không thuộc phạm vi kiến thức của tôi."."""

def get_embedding(text: list[str]) -> list[list[float]]:
    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )
    return [item.embedding for item in response.data]

def get_response(user_message: str, chat_history: list | None = None) -> str:
    if chat_history is None:
        chat_history = []
    chat_history.append({"role": "user", "content": user_message})
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
    assistant_message = response.choices[0].message.content
    chat_history.append({"role": "assistant", "content": assistant_message})
    return assistant_message
