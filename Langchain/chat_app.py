## Conversational Q&A ChatBOT

import os
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
import streamlit as st
load_dotenv()

# Initialising Azure Chat OpenAI
azure_chat_llm = AzureChatOpenAI(
    azure_deployment=os.getenv("OPENAI_DEPLOYMENT_NAME"),
    azure_endpoint=os.getenv("OPENAI_API_BASE"),
    temperature=0.5,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [SystemMessage(content="You are a Comedian AI assistant")]

def get_chatmodel_response(question):

    # Initialising Streamlit Session
    st.session_state['flowmessages'].append(HumanMessage(content= question))
    answer = azure_chat_llm(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content= answer.content))

    return answer.content


## Streamlit UI

# Initialise our Streamlit App
st.set_page_config(page_title="Conversational Q&A ChatBOT")
st.header("Langchain Conversational Chat Application")

# Input Text Box
input = st.text_input("Input: ", key="input")
resp = get_chatmodel_response(input)

# Submit button
submit = st.button("Ask the Question")

# If submit button is clicked
if submit:
    st.subheader("The Response is")
    st.write(resp)