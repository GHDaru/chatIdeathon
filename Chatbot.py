from openai import OpenAI
import streamlit as st
from prompts import *


system = {"role":"system","content":promptSistema}
mensagem = """Olá, amiguinhos! 🌟 Sou o EcoInnovaBot, seu novo companheiro de aventuras pelo incrível mundo da sustentabilidade e energia renovável! 🌱💡

Estou aqui para levar vocês numa jornada cheia de descobertas, diversão e muita criatividade. Juntos, vamos aprender como podemos cuidar do nosso planeta, explorar energias que não acabam e fazer parte de uma grande mudança, tudo isso brincando e criando!

Preparados para serem os super-heróis do meio ambiente? Vamos nessa! Cada pequeno passo que damos faz uma grande diferença. Estou super animado para começar essa aventura com vocês. Vamos lá, equipe EcoInnova! 🌍✨🚀"""

openai_api_key = "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"

st.title("💬 EcoInnovaBot")
st.caption("🚀 ChatBot Educativo by GHD, Brisa e Gabi")

# Função para reiniciar a conversa
def reiniciar_conversa():
    st.session_state["messages"] = [{"role": "assistant", "content": mensagem}, {"role": "assistant", "content": "Bora aprender? Do que quer falar?"}]

# Verifica se a lista de mensagens existe no estado da sessão; se não, inicializa
if "messages" not in st.session_state:
    reiniciar_conversa()

for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.chat_message(msg["role"]).write(msg["content"])

if len(st.session_state.messages)<4:
    opcao = st.radio(
            "E aí, qual vibe você quer explorar hoje?",
            options=["Energia Renovável 🌞", "Vida Sustentável 🌱", "Descobrindo as Energias 🌬️💧🔥", "Desafios e Quizzes 🧠"],
            key='topic_choice'
        )
    st.write(opcao)
    st.session_state.messages.append({"role":"assistant","content":f"Vamos falar sobre o assunto {opcao}"})
    client = OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})

if prompt := st.chat_input(): 
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    client = OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)

# Botão para reiniciar a conversa
if st.button("Reiniciar Conversa"):
    reiniciar_conversa()
