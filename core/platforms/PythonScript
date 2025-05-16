# extract_stream.py
import requests
import re

URL = "https://www.megatv.com/live/"
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(URL, headers=headers)
html = response.text

# Αναζήτηση για πιθανό .m3u8 link
m3u8_match = re.search(r'(https?:\/\/[^\s\'"]+\.m3u8)', html)

if m3u8_match:
    stream_url = m3u8_match.group(1)
    with open("streams.link", "w") as f:
        f.write(stream_url)
    print("✅ Stream link saved:", stream_url)
else:
    print("❌ No stream found.")
