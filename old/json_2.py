from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
client = OpenAI()

user_input = """ tôi tên Lê Thành Đạt 
                năm nay hai mươi hai tuổi"""
system_promt = """
    chuẩn hóa thông tin người dùng: Viết hoa tên.
    Trích xuất thông tin người dùng
"""

class UserData(BaseModel):
    name:str
    age:int

# tao yêu cầu đến OpenAi
resp =  client.responses.parse(
    instructions='Bạn là trích xuất và chuẩn hóa thông tin người dùng',
    model = 'gpt-5.4-mini',
    input=user_input,
    text_format=UserData
)
user = resp.output_parsed
print(f"Ten {user.name}, tuoi: {user.age}")