#-------------IMPORTS- Go below ==========
import youtube_dl
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os, pygame, time
from PIL import Image, ImageTk
from pytube import YouTube
#from io import BytesIO
import subprocess
from tkinter import messagebox



#===========================================
  
cnt=0
#-- - Uploads your local music files (YTB links)-->   USE ONLY ONCE AGAIN WILL MAKE MULTIPLE FILE DOWNLOAD
def progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print("Completion: ", percentage_of_completion)

def convert_songnames(song_names):
    for i in song_names:
        yt = YouTube(i)
        yt.register_on_progress_callback(progress)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download()
    
SONGS= []
def upload_music():   
    songs = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')]    )
    print(songs.split('/')[-1])
    with open(songs, 'r') as f:
        song_names= f.readlines()

    convert_songnames(song_names)
 
#BASIC CONFIG OF BG COLOR WINDOW SIZE AND LOGO
def config_basic(root):     
    # Create main window     
    root.title("MP3 PLAYER")
    root.geometry("400x250")
    root.configure(bg="lightblue")  
    print(os.getcwd())
    # Load the image
    logo_image = ImageTk.PhotoImage(file=r'C:\Users\tejas\OneDrive\Pictures\Desktop\TEJAS-PROFESSIONAL WORKS\MUSICPLAYER-Tejas\logo_1.ico')
    root.iconphoto(False, logo_image)



#xxxxxxxxxxxxxxxxxxxxxx
    # [mp3  ]  ====> FIles only 
#xxxxxxxxxxxxxxxxxxxxxx
song_formats= ('mp3', 'mp4')


def load_music():
    #filter only mp3 files====> only
    global mp3_songs
    mp3_songs= os.listdir()
    mp3_songs= [i for i in mp3_songs if i.endswith(song_formats)]
    print(mp3_songs)
    return mp3_songs
 
def play_music(file):
    #mp3_fo = BytesIO()
    print("PLAYMUSIC",file)

    
    def play_one():
        global cnt
        #subprocess.Popen(['start', '/MIN', eachsong], shell=True)        
        os.startfile(file[cnt])
        time.sleep(1)
        cnt+= 1
         
        return file[cnt]

    play_one()



def hook():

    messagebox.showinfo("Alert", "Contact Developer @Tejas")
    
#HOW TO PAUSE???
def pause_music():
    pass
    
def backward(file):
    print("BACKFILE", file)

    def play_prev():
        global cnt
        #subprocess.Popen(['start', '/MIN', eachsong], shell=True)        
        os.startfile(file[cnt])
        time.sleep(1)
        cnt-= 1
        return file[cnt]

    play_prev()
    

 
#+====  ALL THE BUTTONS, ENTRY LABELS GO BELOW =======
root = tk.Tk()

config_basic(root)


#XXXXXXXxxxxxxxxxXXXXXX
#XX>>>  WIDGETS   <<<<###
            #
            #
            #            
#XXXXXXXxxxxxxxXXXXXXXXXXXXX
#----BUTTONS ---
button = tk.Entry(root,width=300)
button = tk.Label(root, text="Output file path:")
# Create entry widgets for URL and output file path

button = tk.Button(root, text='Open', command=upload_music)
button.place(x=250,y=0)
button.pack(side=tk.TOP, anchor=tk.NE)
#root.state("zoomed")

load_button= tk.Button(root, text='Load', command= load_music)


play_button= tk.Button(root, text='Play/Next',command=lambda: play_music(mp3_songs))




prev_button= tk.Button(root, text='Prev', command=lambda: backward(mp3_songs))

hook_button = tk.Button(root, text="HOOK!", command= hook)
hook_button.pack(pady=20)

play_button.place()
play_button.pack(side=tk.BOTTOM)

 

load_button.place(x=250, y=223)
#load_button.pack(side=tk.BOTTOM)

prev_button.place(x=100, y=223)
#prev_button.pack(x=400, y=190)

#---LABELS ---
root.mainloop()




