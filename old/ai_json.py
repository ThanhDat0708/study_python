from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

user_input = """ Trả về dữ liệu json 
                2 loại trái cây màu xanh lam"""
client = OpenAI()
response = client.responses.create(
    instructions="Chỉ trả về json hợp lệ",
    model = 'gpt-5.4-mini',
    input= user_input,
    text={
        'format':{
            'type':'json_schema'
        }
    }
)

# lấy dữ liệu
print(response.output_text)
