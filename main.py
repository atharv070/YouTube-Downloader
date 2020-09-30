from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
#Creating youtube object with URL
file_size = 0

def progress(stream, chunk, file_handle, remaining=None):
    file_downloaded = (file_size - file_handle)
    per = float((file_downloaded/file_size)*100)
    Dbtn.config(text = "{:00.0f} %Downloaded".format(per))

def startDownload():
    global file_size
    try:
        url = urlFIeld.get()
        print(url)
        Dbtn.config(text='Downloading', state=DISABLED)
        path_to_save = askdirectory()
        print(path_to_save)
        vid = YouTube(url, on_progress_callback=progress)
        strm = vid.streams.first()
        file_size = strm.filesize
        print(file_size)
        VTitle.config(text=strm.title)
        VTitle.pack(side = TOP)
        print("We Found the streams")
        if path_to_save is None:
            return
        else:
            strm.download(path_to_save)
            urlFIeld.delete(0,END)
            showinfo("Download Finished", "Downloaded Successfully")
            VTitle.config(text="")
            Dbtn.config(text="Start Download", state=NORMAL)
    except Exception as e:
        print(e)
        print("Error!!")

def startDownloadT():
    thrd=Thread(target=startDownload)
    thrd.start()

#Started GUI Building
main = Tk()
C = Canvas(main, bg="blue", height=250, width=300)
filename = PhotoImage(file = "bg.png")
background_label = Label(main, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()
main.title("Youtube Video Downloader")

main.iconbitmap('icon.ico')
main.geometry("600x400")
file = PhotoImage(file='icon.png')
HeadingIcon= Label(main, image = file)
HeadingIcon.pack(side= TOP)
urlFIeld = Entry(main,font=("verdana", 20),justify=CENTER)
urlFIeld.pack(side=TOP,fill=X,padx=10)



Dbtn=Button(main, text="Start Download", font= ("verdana",18), relief="ridge",command = startDownloadT)
Dbtn.pack(side=TOP)



