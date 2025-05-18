import requests
from bs4 import BeautifulSoup
import re

def extract_m3u8_links(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    if not response.ok:
        print("Σφάλμα σύνδεσης:", response.status_code)
        return []

    # Αναλύει τη σελίδα
    soup = BeautifulSoup(response.text, 'html.parser')
    links = re.findall(r'(https?://[^\s"\']+\.m3u8)', response.text)
    return links

def generate_m3u_file(links, filename="playlist.m3u"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        for i, link in enumerate(links, start=1):
            f.write(f"#EXTINF:-1,Channel {i}\n{link}\n")
    print(f"Δημιουργήθηκε το αρχείο {filename}")

if __name__ == "__main__":
    page_url = "https://anacon.org/app/cytv.php"
    m3u8_links = extract_m3u8_links(page_url)

    if m3u8_links:
        generate_m3u_file(m3u8_links)
    else:
        print("Δεν βρέθηκαν .m3u8 links.")
