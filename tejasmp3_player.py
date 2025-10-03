#-------------IMPORTS- Go below ==========
import yt_dlp

SONGS = []
#-- Uploads your local music files (YTB links)-->

def convert_songnames(song_names):
    ydl_opts = {
        'format': '140',
        'outtmpl': '%(title)s.%(ext)s'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(song_names)

def upload_music(file):
    #Read text file containing YouTube links and download them
    print("Reading:", file)
    with open(file, 'r') as f:
        song_names = f.readlines()
        print(song_names)
    convert_songnames(song_names)

song_formats = ('mp3', 'mp4')

upload_music('songs.txt')

