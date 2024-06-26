from news_folder.news_api import *
from video_gen.dalle_code import *
from video_gen.gemini_api import *
from video_gen.image_to_video_generator import *
from audio_convert_and_final_video_generator.caption_creater_and_video_audio_merger import *
from audio_convert_and_final_video_generator.text_to_audio_converter import *
from db_functions import *
from chat_query.query import *

def set_query_id(id):
    IdStore.add_id(id)
    print("id stored" + str(id))

def get_query_id():
    return "query id is :"+ IdStore.get_id()

def q_and_a(question):
    id = IdStore.get_id()
    json_path = retrieve_json_path_from_id(id)[0][0]
    answer = file_load(json_path,question)
    return answer

# from dataclasses import dataclass
# @dataclass
# class DataObject:
#     def __init__(self,interest, json_url,video_url):
#         self.interest = interest
#         self.json_url = json_url
#         self.video_url = video_url

class DataObject:
    def __init__(self) -> None:
        interest = ""
        json_url = ""
        video_url = ""
        
def api_and_json_extraction(interests):
    list_of_all_the_json_filepaths = newsapi_fun(interests)
    return list_of_all_the_json_filepaths

def llm_summarizer(json_path):
    summary = file_load_1(json_path)
    return summary

def audio_conv(summary):
    converter(summary)

def dalle_image_gen(summary):
    url = generate_image(summary)
    return url

def video_gen(url):
    if video_gen_fun(url):
        print("video generated and stored in temp folder")
    else:
        print("video generation api failed to generate video")

def final_video_creater():
    video_path = gen_start()
    return video_path

def start_flow(interest):
    data = DataObject()
    data.interest = interest
    list_of_all_json_filepaths = api_and_json_extraction(interest)
    print(list_of_all_json_filepaths)
    for filepath in list_of_all_json_filepaths:
        if filepath == None:
            pass
        else:
            data.json_url = filepath
            summary = llm_summarizer(filepath)
            print(type(summary))
            audio_conv(summary)
            url = dalle_image_gen(summary)
            video_gen(url)
            video_path = final_video_creater()
            data.video_url = video_path
            set_feed_details(data)
        
# start_flow("soccer")