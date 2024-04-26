import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']

def generate_image(prompt, n=1, size="1024x1024"):
    try:
        response = openai.Image.create(
            model="dall-e-2",  # Specify the model version
            prompt=prompt,
            n=n,
            size=size
        )
        images = response.get('data')
        for i, image in enumerate(images):
            # This will print the URL of the generated image
            print(f"Image {i+1}: {image['url']}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
# generate_image("girl in burka")