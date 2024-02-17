from openai import OpenAI
import streamlit as st
from prompts import *

"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"

mensagem = """Olá, amiguinhos! 🌟 Sou o EcoInnovaBot, seu novo companheiro de aventuras pelo incrível mundo da sustentabilidade e energia renovável! 🌱💡

Estou aqui para levar vocês numa jornada cheia de descobertas, diversão e muita criatividade. Juntos, vamos aprender como podemos cuidar do nosso planeta, explorar energias que não acabam e fazer parte de uma grande mudança, tudo isso brincando e criando!

Preparados para serem os super-heróis do meio ambiente? Vamos nessa! Cada pequeno passo que damos faz uma grande diferença. Estou super animado para começar essa aventura com vocês. Vamos lá, equipe EcoInnova! 🌍✨🚀"""

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("💬 EcoInnovaBot")
st.caption("🚀 ChatBot Educativo by GHD, Brisa e Gabi")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role":"system","content":promptSistema},{"role": "assistant", "content": mensagem}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
