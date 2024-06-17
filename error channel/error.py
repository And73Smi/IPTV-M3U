import requests
import m3u8

# Αντικαταστήστε με τη διαδρομή του αρχείου m3u
m3u_file_path = 'path/to/your/iptv.m3u'

# Φόρτωση και ανάλυση του αρχείου m3u
with open(m3u_file_path, 'r') as file:
    m3u_content = m3u8.loads(file.read())

# Έλεγχος κάθε καναλιού
for channel in m3u_content.segments:
    response = requests.head(channel.uri)
    if response.status_code != 200:
        print(f'Error: Channel {channel.uri} is not working')
