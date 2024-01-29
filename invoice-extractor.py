from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini Pro Vision
model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        images_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return images_parts
    else:
        raise FileNotFoundError("No image uploaded")

st.set_page_config(page_title="Invoice Extractor", page_icon=":gem:", layout="wide")

st.header("Gemini Invoice Extractor Application")

input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Upload Image of the invoice: ", type=["png", "jpg", "jpeg"], key="image")

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Invoice', use_column_width=True)

submit = st.button("Tell me about the invoice?")

input_prompt = '''
You are an expert in understanding invoices. We will upload a image of invoice
and you will have to answer any questions based on the uploaded invoice image
'''

if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input, image_data, input_prompt)
    st.subheader("Gemini's Response is: ")
    st.write(response)
