from pytube import YouTube, Playlist


#single links
links = open('links.txt', 'r').readlines()
print links

for i in links:
   i = i[:-1]
   print(i)
   yt=YouTube(i)
   t=yt.streams.filter().all()
   t[0].download()

def getAllLinks(playList):
   allLinks = []
   youtubeLink = 'https://www.youtube.com'
   pl = Playlist(playList)
   for linkprefix in pl.parse_links():
      allLinks.append(youtubeLink + linkprefix)
   return allLinks

# playlist
#for i in getAllLinks('https://www.youtube.com/playlist?list=PLi-mWpouvSohRRb0GETYAD2SUtUCkAjd6'):
#   print(i)


