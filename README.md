# Image Scraper – Download Images from a Website

Script en Python que descarrega totes les imatges (`<img>`) d’una pàgina web i les guarda en una carpeta local.

---

##  Funcionalitat

- Fa una petició HTTP a una URL
- Analitza el contingut HTML amb **BeautifulSoup**
- Extreu tots els atributs `src` de les etiquetes `<img>`
- Converteix URLs relatives en absolutes
- Descarrega les imatges en mode streaming
- Guarda els fitxers en una carpeta local

---

##  Requisits

- Python 3.8+
- Llibreries:
  - `requests`
  - `beautifulsoup4`

Instal·lació:

```bash
pip install requests beautifulsoup4
