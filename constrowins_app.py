# ConstroIA - Versão Avançada com Plano de Ação Inteligente

import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Carrega chave da OpenAI do .env
load_dotenv()
client = OpenAI()

# Layout da interface
st.set_page_config(page_title="ConstroIA", layout="centered")
st.image("logo_constrowins.png", width=200)
st.title("ConstroIA 🧠")
st.markdown("Processador inteligente e estratégico de transcrições da ConstroWins")

# Upload de arquivo
uploaded_file = st.file_uploader("Envie a transcrição da reunião (.txt)", type=["txt"])

if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")

    with st.spinner("Analisando a reunião com a IA..."):
        try:
            prompt = f"""
            Você é uma IA consultora da empresa ConstroWins. Com base na seguinte transcrição de reunião, sua tarefa é:

            1. Organizar os assuntos discutidos por área (RH, Compras, Financeiro, etc).
            2. Para cada item, crie um plano de ação com:
               - Descrição
               - Responsável sugerido (cargo ou função)
               - Prazo estimado (realista)
            3. Destaque pendências importantes que precisam de acompanhamento.
            4. Gere um breve resumo da reunião como se fosse um e-mail a ser enviado ao time.
            5. Ao final, gere uma tabela de acompanhamento com: Área | Tarefa | Responsável | Prazo.

            Aqui está a transcrição:
            {content}
            """

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é uma IA consultora estratégica da ConstroWins."},
                    {"role": "user", "content": prompt}
                ]
            )

            resultado = response.choices[0].message.content
            st.success("Análise concluída!")
            st.markdown("### Resultado da IA:")
            st.write(resultado)

            st.download_button(
                label="📄 Baixar Plano de Ação Inteligente (.txt)",
                data=resultado,
                file_name="plano_acao_inteligente.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"Erro ao processar com a OpenAI: {e}")