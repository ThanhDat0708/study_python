from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client = OpenAI()
chat_histories = []
while True:
    user_input = input("chat gi di:")
    if not user_input:
        break

    chat_histories.append({
        'role':'user',
        'content': user_input
    })
    

    response = client.responses.create(
        model= 'gpt-5.4-mini',
        instructions= 'Chỉ trả kời câu hỏi liên quan toán học và lập trình ',
        input=chat_histories
)
    data = response.output_text
    print(f"Ai tra loi:",data)

    chat_histories.append({
        'role': 'assistant',
        'content' : data
    })