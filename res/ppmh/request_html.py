
import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

def load_url(url):
    reponse = requests.get(url, headers=headers)
    time.sleep(1)
    html = reponse.content.decode("utf-8", errors="ignore")
    return html
