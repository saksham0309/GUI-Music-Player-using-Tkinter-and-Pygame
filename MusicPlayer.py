#Importing Necessary Modules
import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

#creating window (interface) for player
musicplayer = tkr.Tk()

#adding title for interface
musicplayer.title("Music Player")

#setting dimensions of tkinter window
musicplayer.geometry('450x350')

#askdirectory() prompt the user to choose a directory(music directory)
directory = askdirectory()

#os.chdir() method in python is used to change the current working directory to specified path.
# It takes only a single argument as new directory path
os.chdir(directory)

#os.listdir() returns a list conatining the names of the entries in the directory given by path.
songlist = os.listdir()

#creating the playlist
playlist = tkr.Listbox(musicplayer, font = "Arial 14 bold", bg = "cyan2", selectmode=tkr.SINGLE)


#adding songs from songlist to playlist
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos+1

#initializing modules
pygame.init()
pygame.mixer.init()

#function for play button
def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

#function for stop button
def ExitMusicPlayer():
    pygame.mixer.music.stop()

#funtion for pause button
def pause():
    pygame.mixer.music.pause()

#function for resume button
def resume():
    pygame.mixer.music.unpause()

#Creating buttons
Button1 = tkr.Button(musicplayer, width=5, height=1, font="Arial 20 bold", text="Play Music", command=play, bg="green", fg="black")

Button2 = tkr.Button(musicplayer, width=5, height=1, font="Arial 20 bold", text="Stop Music", command=ExitMusicPlayer, bg="red", fg="black")

Button3 = tkr.Button(musicplayer, width=5, height=1, font="Arial 16 bold", text="Pause Music", command=pause, bg="yellow", fg="black")

Button4 = tkr.Button(musicplayer, width=5, height=1, font="Arial 16 bold", text="Resume Music", command=resume, bg="skyblue", fg="black")

var = tkr.StringVar()

songtitle = tkr.Label(musicplayer, font="Arial 12 bold", textvariable=var)

songtitle.pack()

Button1.pack(fill="x")

Button2.pack(fill="x")

Button3.pack(fill="x")

Button4.pack(fill="x")

playlist.pack(fill="both", expand="yes")

musicplayer.mainloop()