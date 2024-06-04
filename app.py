import streamlit as st

import google.generativeai as genai

from dotenv import load_dotenv

import os 

load_dotenv()

#load the api key 
genai.configure(os.env(api_key="GOOGLE_API_KEY"))

#function to load gemini pro model and get response

model=genai.GenerativeModel('gemini-pro')

chat=model.start_chat(history=[])

#question send it to LLM model
def gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response

##initialilze our streamlit app

st.set_page_config(page_title="Q and A Demo")

st.header("Gemini LLM application")

#Initialize session state for chat history if it doesn't exit

if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]

input=st.text_input("Input",key="input")

submit=st.button("Ask the question ")

if submit and input:
    response=gemini_response(input)

    ## Add user query and response to session chat history
    #to store all entire history
    st.session_state['chat_history'].append(('you',input)) #storing all session inside you
    st.subheader("The response is ")
    
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(('Bot',chunk.text))
st.subheader("the chat history is")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")




