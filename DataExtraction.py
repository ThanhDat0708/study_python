from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

client = OpenAI()
user_input = """
            Hôm qua khách Nguyễn Văn A (tuổi 30) gọi điện.
            Bảo là thích chơi thể thao. 
            Gửi email xác nhận qua nguyenvana@email.com, SDT là 012345678.
"""
class UserData(BaseModel):
    name: str
    age: int
    hoppy: str
    addr: str
    phone: int
resp = client.responses.parse(
    instructions= """Bạn hãy trích xuất thông tin người dùng tên tuổi số điện thoại
            sở thích địa chỉ email.""",
    model= 'gpt-5.4-mini',
    input=user_input,
    text_format=UserData
                    
    
)
user = resp.output_parsed
print(f"Ten:{user.name},Tuoi: {user.age}, so thich:{user.hoppy}, email:{user.addr}, phone:{user.phone}")
