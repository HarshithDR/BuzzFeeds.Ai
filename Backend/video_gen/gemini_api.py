import google.generativeai as genai
import os
from dotenv import load_dotenv
import json

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

def summariaze(prompt):
    response = model.generate_content(prompt + '/n Summariaze the above content in 2 sentences or 100 words')
    return response.text

def file_load(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        captions_data = json.load(f)

    summary = summariaze(captions_data['content'])
    print(summary)
    return summary

# example usage
# print(summariaze('what is the meaning of life?'))