from helpers.streamlit_chat_helper import streamlit_chat_helper

def chat_with_llm(user_message):
    return f"You said: {user_message}"


if __name__ == "__main__":
    streamlit_chat_helper(chat_with_llm)
