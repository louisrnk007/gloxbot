import requests
from bs4 import BeautifulSoup

URL = "https://glowcheek.fr/faq/"

def scraper_glowcheek():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "lxml")

    faq_sections = soup.select(".elementor-widget-container")  # à ajuster selon la page
    contenu = ""

    for section in faq_sections:
        text = section.get_text(separator="\n").strip()
        contenu += text + "\n\n"

    with open("data/glowcheek_data.txt", "w", encoding="utf-8") as f:
        f.write(contenu)

if __name__ == "__main__":
    scraper_glowcheek()
    print("✅ Données GlowCheek extraites avec succès.")
