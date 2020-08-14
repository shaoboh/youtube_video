import requests, os

Root_url = "http://play.taihe.com/data/music/songlink"
From_data = {'songIds': '242078437'}

response = requests.post(url = Root_url, data = From_data)
music_info = response.json()['data']['songList'][0]

albumName = music_info['albumName']
artistName = music_info['artistName']
lrcLink = music_info['lrcLink']
songLink = music_info['songLink']
songName = music_info['songName']

# path = 'D:\\temp\\'
# os.chdir(path)
# os.mkdir(artistName)
# os.chdir(path + artistName)
# os.mkdir(albumName)
# os.chdir(path + artistName + "\\" + albumName)

print("正在保存歌曲：" + songName)
response = requests.get(songLink)
with open(songName + '.mp3', 'wb') as f:
    f.write(response.content)

#print("正在保存歌词...")
response = requests.get(lrcLink)
with open(songName + '.lrc', 'wb') as f:
    f.write(response.content)
print("执行完毕...")