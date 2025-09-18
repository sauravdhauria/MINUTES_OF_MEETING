import google.generativeai as genai
import os
import cv2
from PIL import Image
import numpy as np

def extract_text_image(image_path):
    file_bytes = np.asarray(bytearray(image_path.read()),dtype=np.uint8)
    image=cv2.imdecode(file_bytes,cv2.IMREAD_COLOR)
    #lets load and preprocess the image
    #image = cv2.imread('Capture1.png')
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB) # To convert BGR to RGB
    image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # To convert BGR to Grey
    _,image_bw = cv2.threshold(image_grey, 150, 255, cv2.THRESH_BINARY) # To convert Grey to Black and White


    # The image that CV2 give is in numpy array format,we need to convert it image object
    final_image = Image.fromarray(image_bw) 

    # configure genai model
    key =os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=key)
    model = genai.GenerativeModel('gemini-2.5-flash-lite')


    #lets write prompt for OCR
    prompt = """You act as an OCR application on the given image and extract the text from it.
           Give only the text as output without any other explanation. or description."""


    #lets extract and return the text
    response = model.generate_content([prompt,final_image])
    output_text = response.text
    return output_text
    
