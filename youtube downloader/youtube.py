from tkinter import *
from pytube import YouTube


def Download():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(yt, text='DOWNLOADED', font='arial 15').place(x=180, y=210)


yt = Tk()
yt.geometry('800x600')
yt.title('Youtube Video Downloader')
# Title for the label
Label(yt, text='Youtube Video Downloader', font=('helvetica', 20, 'bold')).pack()
# entry to paste the link into
link = StringVar(yt)
link_entry = Entry(yt, textvariable=link, width=80).place(x=32, y=90)
# Button to run the download command
run_download = Button(yt, text='Download', width=10, bg='white', command=Download).place(x=180, y=150)

yt.mainloop()
