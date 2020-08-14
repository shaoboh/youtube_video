# Version: V1.0.0
# Brief: tool to scrapy youtube video
# Author: James_Bobo
# ModifyUpdate:
# # VersionUpdateInfo:

import pafy

# class YoutubeVideoDownload():
#     '''
#     @brief:下载Youtube视频
#     '''
#     def __init__(self,url):
#         self.download_url = url  #绑定到url

#     def runDownload(self,save_path):
#         self.save_path = save_path #设置保存路径
#         #开始下载
#         video = pafy.new(self.download_url)
#         v_best =video.getbest() #下载最清晰画质
#         v_best.download(self.save_path)

# # 使用该类的方法
# if __name__ == '__main__':
#     '''调用方法示例'''
#     # you=YoutubeVideoDownload()
#     # you.runDownload()
#     youtube = YoutubeVideoDownload('https://www.youtube.com/watch?v=gscxgzQvwUU') #先实例化该类，设置需要下载的url
#     youtube.runDownload('E:\\James\\code\\spider\\') #设置保存路径，并执行下载

# download_url = 'https://www.youtube.com/watch?v=gscxgzQvwUU'
# download_url = 'https://www.youtube.com/watch?v=hmNHEFvv56A'
# save_path = 'E:\\James\\code\\spider\\'
# video = pafy.new(download_url)
# v_best =video.getbest()
# v_best.download(save_path)
####################################################################################
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
