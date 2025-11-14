import streamlit as st
import requests
import random
import time
       
def response_generator(user_input):
    '''Expects a user input string, generates responses from the ollama backend 
    yields response words one by one'''
    response = requests.post(
                "http://localhost:8000/chat",
                json={"text": user_input},
                timeout=2000
            )
    if response.status_code == 200:
        for word in response.json()['response'].split():
            yield word + " "
            time.sleep(0.05)
    else: 
        for word in response.text.split():
            yield word + " "
            time.sleep(0.05)


st.title("Example Corp Hospitality Group Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Please enter your query?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

