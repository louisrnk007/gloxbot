import requests
from bs4 import BeautifulSoup
import json
import os

URL = "https://glowcheek.fr/faq/"

def scrap_faq():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")

    faq = []
    questions = soup.find_all("h4")
    answers = soup.find_all("div", class_="toggle-content")

    for q, a in zip(questions, answers):
        faq.append({
            "question": q.get_text(strip=True),
            "answer": a.get_text(strip=True)
        })

    # Stocker le fichier dans data/
    os.makedirs("data", exist_ok=True)
    with open("data/faq.json", "w") as f:
        json.dump(faq, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    scrap_faq()
