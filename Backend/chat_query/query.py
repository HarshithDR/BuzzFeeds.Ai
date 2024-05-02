import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
import requests

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

def summariaze(body):
    response = model.generate_content(body + '/n Summariaze the above content in 2 sentences or 100 words')
    return response.text

def file_load(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        captions_data = json.load(f)

    summary = summariaze(captions_data['content'])
    print(summary)
    return summary

def questions_query(url):
    

# example usage
# print(summariaze('what is the meaning of life?'))