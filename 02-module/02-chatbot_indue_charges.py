from langchain_google_vertexai import ChatVertexAI
from helpers.models_name import VERTEXAI_MODELS
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from helpers.streamlit_chat_helper import streamlit_chat_helper
from helpers.agents_prompts import PROMPTS
from helpers.local_history import load_chat_history, save_chat_history

def chat_with_llm(user_message) -> str:
    history_file_path = "123_local_history.json"
    history = load_chat_history(history_file_path)
    history.append({"role": "user", "content": user_message})
    prompt = "You are a mathematician, be very precise and answer the question"

    # equivalent to [("system", prompt), ...("history"), (user, new_message)]
    prompt_template = ChatPromptTemplate([
        ("system", prompt),
        MessagesPlaceholder("messages_history")
    ])

    chain = prompt_template | ChatVertexAI(model_name=VERTEXAI_MODELS.GEMINI_1_5_FLASH)
    response = chain.invoke({"messages_history": history})

    history.append({"role": "assistant", "content": response.content})
    save_chat_history(history, history_file_path)


    for message in history:
        print(f"{message['role']}: {message['content']}\n")

    return response.content

if __name__ == "__main__":
    streamlit_chat_helper(
        chat_with_llm,
        title="Matematician",
        description_md="",
    )



