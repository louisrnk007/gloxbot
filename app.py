import streamlit as st
import openai

st.set_page_config(page_title="GlowBot", page_icon="💄", layout="centered")

st.title("💬 GlowBot - Assistant GlowCheek")
st.markdown("Posez-moi une question sur nos produits, la livraison ou nos offres !")

openai.api_key = st.secrets["openai"]["api_key"]

def repondre_glowcheek(question):
    contexte = (
        "GlowCheek est une marque de soins visage qui propose des masques raffermissants, "
        "accessoires beauté et produits sculptants. Le masque signature aide à affiner les contours "
        "du visage et donne des résultats visibles dès 2 semaines pour 84% des utilisateurs. "
        "La livraison est gratuite et rapide, les produits sont disponibles pour hommes et femmes. "
        "GlowCheek est régulièrement en rupture de stock en raison de la forte demande."
    )

   from openai import OpenAI

client = OpenAI(api_key=st.secrets["openai"]["api_key"])  # sécurisé avec Streamlit secrets

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Tu es l'assistant de la boutique GlowCheek. Réponds aux clients en te basant uniquement sur les produits et infos du site."},
        {"role": "user", "content": question}
    ]
)

reponse = chat_completion.choices[0].message.content

    return completion.choices[0].message.content

question = st.text_input("Votre question :", placeholder="Ex: Quels sont les bienfaits du masque GlowCheek ?")

if question:
    with st.spinner("GlowBot réfléchit..."):
        reponse = repondre_glowcheek(question)
        st.success(reponse)
