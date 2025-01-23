import streamlit as st
import time
from typing import Callable

class StreamlitChatMessage:
    def __init__(self, role, content):
        self.role = role
        self.content = content


def streamlit_chat_helper(
    generate_response: Callable[[str], str],
    title: str = "Chatbot",
    description_md: str = """
    ### How to use this chat:
    1. Type your message in the input box below
    2. Press Enter or click the send button
    3. Wait for the assistant's response

    **Example interactions:**
    - "Hello, how are you?"
    - "Tell me about yourself"
    """
):
    st.title(title)
    st.markdown(description_md)

    #create message if not exists
    if "messages" not in st.session_state:
        st.session_state.messages = []

    #display messages
    for message in st.session_state.messages:
        with st.chat_message(message.role):
            st.markdown(message.content)


    #user input
    if user_message := st.chat_input("Enter your message"):
        st.session_state.messages.append(StreamlitChatMessage(role="user", content=user_message))
        with st.chat_message("user"):
            st.markdown(user_message)


    if user_message:
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            with st.spinner("Thinking..."):
                response = generate_response(user_message)
                new_message = StreamlitChatMessage(role="assistant", content=response)
                message_placeholder.markdown(new_message.content)
                st.session_state.messages.append(new_message)

if __name__ == "__main__":
    streamlit_chat_helper(lambda x: "... false this")
