import streamlit as st
from openai import OpenAI

# Initialise le client OpenAI (version à jour)
client = OpenAI(api_key=st.secrets["openai"]["api_key"])

def repondre_glowcheek(question):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Tu es l’assistant du site GlowCheek. Tu donnes des réponses uniquement à partir des infos du site. Si tu ne sais pas, dis-le simplement."},
            {"role": "user", "content": question}
        ]
    )
    return completion.choices[0].message.content

st.title("💬 GlowBot - Assistant GlowCheek")
st.write("Posez-moi une question sur nos produits, la livraison ou nos offres !")

question = st.text_input("Votre question :")

if question:
    response = repondre_glowcheek(question)
    st.write("**GlowBot :**", response)
