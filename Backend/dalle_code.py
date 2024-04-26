# use this code as reference to integrate dalle
import openai

# Your OpenAI API key
openai.api_key = 'sk-proj-mqjm2SJlMwbAiA68xN5vT3BlbkFJlp04U7rxJERJM1W0JqnF'

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
generate_image("A futuristic cityscape at sunset, vivid colors, hyper-detailed, digital art")
