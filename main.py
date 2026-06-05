from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()
while True:
    user_input = input("chat gi di (exit=0):")
    if user_input == '0':
        break
    response = client.responses.create(
        model= 'gpt-5.4-mini',
        input= user_input
)
    data = response.output_text
    print("Ai tra loi:",data)