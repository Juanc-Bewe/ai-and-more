from langchain_google_vertexai import ChatVertexAI
from helpers.models_name import VERTEXAI_MODELS
from langchain_core.prompts import ChatPromptTemplate
from helpers.streamlit_chat_helper import streamlit_chat_helper
from helpers.agents_prompts import PROMPTS


def chat_with_llm(user_message) -> str:
    prompt = PROMPTS.IG_NOBEL_EXPERT

    # Remove extra whitespace and normalize line breaks
    # formatted_prompt = ' '.join(line.strip() for line in prompt.splitlines() if line.strip())

    prompt_template = ChatPromptTemplate.from_messages(
        [("system", prompt), ("user", "{input}")]
    )

    # equivalent to
    # prompt_template_injected = prompt_template.invoke({"input": user_message}) # and then
    # llm = ChatVertexAI(model_name=VERTEXAI_MODELS.GEMINI_1_5_FLASH) # and then
    # response = llm.invoke(prompt_template_injected)

    chain = prompt_template | ChatVertexAI(model_name=VERTEXAI_MODELS.GEMINI_1_5_FLASH)
    response = chain.invoke({"input": user_message})
    return response.content


if __name__ == "__main__":
    streamlit_chat_helper(
        chat_with_llm,
        title="",
        description_md="""
            ### ¡Bienvenido al Chat Experto en Premios Ig Nobel!
            Pregúntame sobre el fascinante mundo de los premios Ig Nobel - investigaciones que primero te hacen reír y luego te hacen pensar.

            **Ejemplos de preguntas:**
            - "Cuéntame sobre el estudio de por qué los pájaros carpinteros no tienen dolor de cabeza"
            - "¿Cuál ha sido el premio más extraño jamás otorgado?"
            - "Explícame la investigación sobre nadar en jarabe vs agua"
            - "Háblame sobre la física de caminar con café"
            - "Medicina"
        """,
    )
