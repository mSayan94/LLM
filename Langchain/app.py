# Q&A ChatBOT

import os
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI
import streamlit as st
load_dotenv()

# Function to load OpenAI model and get response


def get_openai_response(question):

    # Initialising Azure Chat OpenAI
    azure_chat_llm = AzureChatOpenAI(
        azure_deployment=os.getenv("OPENAI_DEPLOYMENT_NAME"),
        azure_endpoint=os.getenv("OPENAI_API_BASE"),
        temperature=0.5,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    response = azure_chat_llm.predict(question)
    return response


# Initialise our Streamlit App
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Chat Application")

# Input Text Box
input = st.text_input("Input: ", key="input")
resp = get_openai_response(input)

# Submit button
submit = st.button("Ask the Question")

# If submit button is clicked
if submit:
    st.subheader("The Response is")
    st.write(resp)
