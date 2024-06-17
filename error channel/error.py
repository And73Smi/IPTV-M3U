import requests
from m3u8 import M3U8

# Αντικαταστήστε με τη διαδρομή του αρχείου m3u
m3u_file_path = 'iptv.m3u'

# Φόρτωση και ανάλυση του αρχείου m3u
with open(iptv.m3u 'r') as file:
    m3u_content = M3U8(file.read())

# Έλεγχος κάθε καναλιού
for channel in m3u_content.segments:
    response = requests.head(channel.uri)
    if response.status_code != 200:
        print(f'Error: Channel {no work} is not working')
