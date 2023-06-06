from pytube import YouTube
import sys

if len(sys.argv) < 2:
    print("Usage: python <script_name>.py <youtube_link>")
    sys.exit(1)

link = sys.argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()
yd.download(r"C:\Users\Mitko\Desktop\videos")

#for at køre programmet: terminal: python YoutubeDownloader.py "youtube link"
  
