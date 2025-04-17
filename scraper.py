import requests
from bs4 import BeautifulSoup

def scraper_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # On récupère les titres et paragraphes
    titres = soup.find_all(['h1', 'h2', 'h3'])
    paragraphes = soup.find_all(['p', 'li'])

    contenu = ""
    for titre in titres:
        contenu += f"\n## {titre.get_text(strip=True)}\n"
    for p in paragraphes:
        texte = p.get_text(strip=True)
        if texte:
            contenu += f"{texte}\n"

    return contenu

# Exemple d'URL produit sur GlowCheek
url = "https://glowcheek.fr/products/masque-face-form"
contenu_scrape = scraper_page(url)

# On sauvegarde dans un fichier local
with open("data/masque_face_form.txt", "w", encoding="utf-8") as f:
    f.write(contenu_scrape)

print("✅ Données extraites et enregistrées.")
