from langchain_google_vertexai import ChatVertexAI
from langchain_ollama import ChatOllama
from helpers.streamlit_chat_helper import streamlit_chat_helper
from helpers.models_name import VERTEXAI_MODELS
from langchain.schema import HumanMessage

def chat_with_vertexai(user_message):
    llm = ChatVertexAI(model_name=VERTEXAI_MODELS.GEMINI_1_5_FLASH)
    response = llm.invoke([HumanMessage(content=user_message)])
    return response.content

def chat_with_ollama(user_message):
    llm = ChatOllama(model="llama3.2")
    response = llm.invoke([HumanMessage(content=user_message)])
    return response.content

if __name__ == "__main__":
    streamlit_chat_helper(chat_with_ollama)

