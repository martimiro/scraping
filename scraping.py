import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def getdata(url):
    r = requests.get(url)
    r.raise_for_status()
    return r.text

def download_image(img_url, folder):
    try:
        response = requests.get(img_url, stream=True)
        response.raise_for_status()

        filename = os.path.basename(img_url.split("?")[0])
        filepath = os.path.join(folder, filename)

        with open(filepath, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"Saved: {filename}")

    except Exception as e:
        print(f"Failed to download {img_url} - {e}")

url = "link_to_web"
folder = "folder_name"

os.makedirs(folder, exist_ok=True)

htmldata = getdata(url)
soup = BeautifulSoup(htmldata, 'html.parser')

for item in soup.find_all('img'):
    src = item.get('src')
    if not src:
        continue

    img_url = urljoin(url, src)
    download_image(img_url, folder)
