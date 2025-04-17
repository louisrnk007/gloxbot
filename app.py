import streamlit as st
import openai

st.set_page_config(page_title="GlowBot", layout="centered")
st.title("💬 GlowBot - Assistant GlowCheek")
st.write("Posez-moi une question sur nos produits, la livraison ou nos offres !")

# Lire les données scrappées
with open("data/glowcheek_data.txt", "r", encoding="utf-8") as f:
    base_connaissance = f.read()

# Champ utilisateur
question = st.text_input("Votre question :")

if question:
    with st.spinner("GlowBot réfléchit..."):
        client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])

        prompt = f"""
Tu es l'assistant GlowBot de la marque GlowCheek. Voici les infos dont tu disposes :

{base_connaissance}

Réponds à cette question de façon claire et précise :
{question}
"""

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        st.markdown("**GlowBot** : " + response.choices[0].message.content)
