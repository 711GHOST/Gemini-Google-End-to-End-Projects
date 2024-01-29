from dotenv import load_dotenv
load_dotenv() # Loading all the environment variables


import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemeni Pro Model and get responses


model = genai.GenerativeModel('gemini-pro')
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


## setting up the streamlit app
st.set_page_config(page_title="Gemini Pro", page_icon=":gem:", layout="wide")

st.header("Gemini Pro LLM Application")

input = st.text_input("Enter your question here", key="input")
submit = st.button("Ask the Question?")

## When Submit is clicked

if submit:
    response = get_gemini_response(input)
    st.subheader("Response is: ")
    st.write(response)