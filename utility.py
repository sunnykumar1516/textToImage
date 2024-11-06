
import requests
import os


secret_key = os.getenv("HF_TOKEN")
#secret_key = "Bearer "+ secret_key

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large"
headers = {"Authorization": secret_key}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

# You can access the image with PIL.Image for example

import io
from PIL import Image
def getImage(text):
    image_bytes = query({
	"inputs": text,
    })
    image = Image.open(io.BytesIO(image_bytes))
    return image
