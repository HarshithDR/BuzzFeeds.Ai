import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

def summariaze(prompt):
    response = model.generate_content(prompt)
    return response.text

# example usage
# print(summariaze('what is the meaning of life?'))