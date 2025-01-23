import helpers as hps
from langchain_google_vertexai import ChatVertexAI
from langchain_ollama import ChatOllama
from langchain.schema import HumanMessage
from helpers.models_name import VERTEXAI_MODELS

def call_llm():
    user_input = hps.get_user_input()

    # llm = ChatVertexAI(
    #     model_name=VERTEXAI_MODELS.GEMINI_1_5_FLASH_002,
    #     temperature=0,
    # )

    llm = ChatOllama(
        model="llama3.2",
        temperature=0,
    )

    response = llm.invoke([HumanMessage(content=user_input)])
    print("🤖 LLM Response:\n")
    print(response.__repr__())
    print(f"\n{response.content}\n")



if __name__ == "__main__":
    call_llm()
