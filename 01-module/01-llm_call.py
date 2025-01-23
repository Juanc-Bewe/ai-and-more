import helpers as hps
from langchain_google_vertexai import ChatVertexAI
from langchain.schema import HumanMessage


def call_llm():
    user_input = hps.get_user_input()

    llm = ChatVertexAI(
        model_name=hps.VERTEXAI_MODELS.GEMINI_1_5_FLASH,
        temperature=0,
    )

    response = llm.invoke([HumanMessage(content=user_input)])
    print("🤖 LLM Response:\n")
    print(response.__repr__())
    print(f"\n{response.content}\n")



if __name__ == "__main__":
    call_llm()
