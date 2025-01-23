import helpers as hps
from langchain_google_vertexai import ChatVertexAI

def call_llm():
    user_input = hps.get_user_input()

    llm = ChatVertexAI(
        model_name="gemini-1.5-flash-002",
        temperature=0.0,
    )

    response = llm.invoke(user_input)
    print("🤖 LLM Response:\n")
    print(response.__repr__())
    print("\n")



if __name__ == "__main__":
    call_llm()
