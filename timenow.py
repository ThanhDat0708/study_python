from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime

def get_current_datatime():
    """Trả về thời gian hiện tại của thiết bị"""
    now = datetime.now()
    str_now = now.strftime("%d/%m/%Y %H:%M")
    return f"Bây Giờ là {str_now}"
tools = [
    {  
        "type": "function",
        "name": "get_current_datatime",
        "description": " lấy thời gian hiện tại",
        "strict": False
        
    }
]

load_dotenv()
client = OpenAI()
chat_histories = []
while True:
    user_input = input("chat:")
    if not user_input:
        break
    chat_histories.append(
        {
            'role':'user',
            'content': user_input
        }
    )

    response = client.responses.create(
        model='gpt-5.4-mini',
        input=chat_histories,
        temperature=0.1,
        max_output_tokens=500,
        tools=tools
    )

    # kiểm tra gọi hàm nếu có
    is_function_calling = False
    ai_reply = ""
    for item in response.output:
        if item.type == 'function_call':
            if item.name == 'get_current_datatime':
                is_function_calling = True
                ai_reply = get_current_datatime()

    if not is_function_calling:
        ai_reply = response.output_text

    print(f"AI phản hồi: {ai_reply}")

    chat_histories.append({
        'role': 'assistant',
        'content': ai_reply
    })

def get_current_datatime():
   return datetime.now().strftime("%d/%m/%Y %H:%M")