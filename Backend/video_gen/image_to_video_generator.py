import fal_client
import os
import requests
from dotenv import load_dotenv

load_dotenv()
FAL_API_KEY = os.environ["FAL_API_KEY"]

def fal_api_fun(url):
    os.environ["FAL_KEY"] = FAL_API_KEY
    handler = fal_client.submit(
        "fal-ai/fast-svd",
        arguments={
            "image_url": url
        },
    )
    log_index = 0
    for event in handler.iter_events(with_logs=True):
        if isinstance(event, fal_client.InProgress):
            new_logs = event.logs[log_index:]
            for log in new_logs:
                print(log["message"])
            log_index = len(event.logs)

    result = handler.get()
    print ('result')
    return result

def download_video(url, save_dir):
    try:
        response = requests.get(url, stream=True)
        filename = 'output_video' + ".mp4"  # Generate a random filename
        save_path = os.path.join(save_dir, filename)
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        print(f"Video downloaded successfully to {save_path}!")
    except Exception as e:
        print(f"Error downloading video: {e}")

def video_gen_fun(url):
    url_from_fal = fal_api_fun(url)
    print(url_from_fal)
    parsed_data = url_from_fal
    video_url = parsed_data['video']['url']
    save_path = "Backend/audio_convert_and_final_video_generator/temp_files/"
    download_video(video_url,save_path)
    return True

# video_gen_fun("https://oaidalleapiprodscus.blob.core.windows.net/private/org-rf5d3q6Q0Izis4bDLs1K9N2S/user-LA72cJO45AStPYS1p3YjxPNA/img-GlMPlynDSRnxLRfY2yDvNpQ1.png?st=2024-04-26T06%3A56%3A39Z&se=2024-04-26T08%3A56%3A39Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-04-26T05%3A47%3A31Z&ske=2024-04-27T05%3A47%3A31Z&sks=b&skv=2021-08-06&sig=k2yXx/t9%2BSJ8AHY5gro4G0p0u9oa%2BtzvoGX%2BoWGcZGU%3D")