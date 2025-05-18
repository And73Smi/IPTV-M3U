import os

def generate_m3u(directory):
    """
    Διαβάζει τα .m3u8 αρχεία στον φάκελο `directory` και δημιουργεί ένα .m3u αρχείο.
    """
    output_file = "streams/iptv_channels.m3u"
    
    # Άνοιγμα του αρχείου εξόδου για εγγραφή
    with open(output_file, 'w') as f_out:
        f_out.write("#EXTM3U\n")  # Ξεκινάμε το αρχείο M3U

        # Βρόχος για να περάσουμε όλα τα αρχεία στον φάκελο `directory`
        for filename in os.listdir(directory):
            if filename.endswith(".m3u8"):
                stream_name = filename.replace(".m3u8", "").replace("_", " ").title()  # Δημιουργία του τίτλου
                file_path = os.path.join(directory, filename)
                
                # Προσθήκη πληροφοριών στο .m3u
                f_out.write(f"#EXTINF:-1,{stream_name}\n")
                f_out.write(f"{file_path}\n")
    
    print(f"M3U file created: {output_file}")

if __name__ == "__main__":
    # Ο φάκελος στον οποίο βρίσκονται τα .m3u8 αρχεία
    directory = "streams"
    generate_m3u(directory)
