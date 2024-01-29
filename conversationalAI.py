from dotenv import load_dotenv
load_dotenv() # Loading all the environment variables


import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemeni Pro Model and get responses


model = genai.GenerativeModel('gemini-pro')

# To store history of chat
chat = model.start_chat(history=[])

# Get Response from Gemini Pro
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

## setting up the streamlit app
st.set_page_config(page_title="Gemini Pro", page_icon=":gem:", layout="wide")

st.header("Gemini Pro LLM Application")

# Initialize the session state to store the history of chat if it doesn't exist
if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = [] # Name od the session state is chat_history

input = st.text_input("Input", key="input")
submit = st.button("Ask the Question?")

## When Submit is clicked

if submit and input:
    response = get_gemini_response(input)
    # Add user query and response to session chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("Response is: ")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.subheader("Chat History is:")

for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")