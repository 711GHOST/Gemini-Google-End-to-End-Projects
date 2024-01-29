from dotenv import load_dotenv
load_dotenv() # Loading all the environment variables


import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemeni Pro Model and get responses


model = genai.GenerativeModel('gemini-pro-vision')
def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="Gemini Pro Vision", page_icon=":gem:", layout="wide")

st.header("Gemini Pro Vision LLM Application")

input = st.text_input("Enter your question here", key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit = st.button("Ask the Question?")

## When Submit is clicked

if submit:
    response = get_gemini_response(input, image)
    st.subheader("Response is: ")
    st.write(response)