import google.generativeai as genai
import os
from dotenv import load_dotenv
import json

class IdStore:
    id = 0
    @classmethod
    def add_id(cls, id):
        cls.id = id

    @classmethod
    def get_id(cls):
        return cls.id

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

def answer_fun(body,question):
    response = model.generate_content(body + '/n Refer the above content and answer the below question  /n' + question)
    return response.text

def file_load(json_path,question):
    with open(json_path, 'r', encoding='utf-8') as f:
        captions_data = json.load(f)

    answer = answer_fun(captions_data['content'],question)
    print(answer)
    return answer

    
# example usage
# print(summariaze('what is the meaning of life?'))