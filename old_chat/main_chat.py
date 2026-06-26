
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def chat_fn(mesg: str, history:list) ->str:
    message =[]

    for m in history:
        message.append({
            "role": m["role"],
            "content": m["content"][0]["text"]
        })
    message.append({
        "role":"user",
        "content": mesg
    })
     
    response = client.responses.create(
        model='gpt-5.4-mini',
        input=message,
        temperature=0.1,
        max_output_tokens=500
    )
    return response.output_text

