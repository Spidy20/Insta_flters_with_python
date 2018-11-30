import tkinter as tk
from pytube import YouTube

def download():
    global E1
    global yt
    data = E1.get()
    y=YouTube(str(data))
    # YouTube(str(yt)).streams.first().download('C:/Users/kusha/PycharmProjects/Filters_cv/images')


root=tk.Tk()
w=tk.Label(root,text="Youtube Downloader")
w.pack()
E1=tk.Entry(root,bd=5)
E1.pack(side=tk.TOP)
button=tk.Button(root,text="Download",fg="red",command= download  )
button.pack(side=tk.BOTTOM)
root.mainloop()

