# Version: V1.0.0
# Brief: tool to scrapy youtube video
# Author: James_Bobo
# ModifyUpdate:
# # VersionUpdateInfo:
import os
# "--skip-download", 
def download_subs(video_url, lang="en_US"):
    cmd = [
        "youtube-dl",
        "--write-auto-sub",
        "--embed-subs",
        "--sub-lang",      
        lang,
        video_url
    ]

    os.system(" ".join(cmd))


url = "https://www.youtube.com/watch?v=gscxgzQvwUU"
# url = "https://www.youtube.com/watch?v=2RN6mObJV6U"
url = "https://www.youtube.com/watch?v=mwKWD0yDHDw"
download_subs(url)
