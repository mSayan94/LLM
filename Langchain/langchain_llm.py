from langchain.llms import HuggingFaceHub
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv(".env")

api_token = os.getenv("HUGGINGFACE_API_TOKEN")
model_name = os.getenv("HUGGINGFACE_MODEL_NAME")

print(api_token)
print(model_name)

llm = HuggingFaceHub(
    huggingfacehub_api_token = api_token, repo_id=model_name, model_kwargs={"max_length": 128, "temperature": 0.5}
)
# llm_chain = LLMChain(prompt=prompt, llm=llm)
print(llm.predict("Who is the President of India"))