import os
import threading
from tkinter import SUNKEN
import customtkinter as ctk
from customtkinter import filedialog
from PIL import Image
import socket   
hostname=socket.gethostname()   
IPAddr=str(socket.gethostbyname(hostname))
# window 
app = ctk.CTk()
app.title('HTTP File Share App')
app.geometry('800x600')
def servec():
    os.system("python -m http.server "+str(port))
def serverclose():
    os.system("taskkill /F /im python.exe")
def hshare() :
    global path,flab
    path = str(filedialog.askdirectory())
    st=("Selected Path: "+path)
    flab= ctk.CTkLabel (
        master=frame,
        text=st,
        font=("Arial",15),
        fg_color="transparent",
        text_color="#D1F2EB",
    )
    flab.pack()
def serve():
    global port,t
    os.chdir(path)
    if portbox.get()=='':
        port=9999
    else:
        port=portbox.get()
    t = threading.Thread(target=servec, daemon=True)
    t.start()
    app.destroy()            # destroy current window and creating new one 
    w = ctk.CTk()  
    w.geometry("800x600")
    w.title('Server Started')
    l1=ctk.CTkLabel(master=w, text="Your Host Name",text_color="#1ABC9C",font=('Century Gothic',30))
    l2=ctk.CTkLabel(master=w, text=hostname,text_color="#5DADE2",font=('Century Gothic',30))
    l3=ctk.CTkLabel(master=w, text="Your IP Address",text_color="#F5B041",font=('Century Gothic',30))
    l4=ctk.CTkLabel(master=w, text=IPAddr,text_color="#F1948A",font=('Century Gothic',30))
    shpath=("Your Shared Path: "+path)
    l5=ctk.CTkLabel(master=w, text=shpath,text_color="#BB8FCE",font=('Century Gothic',30))
    fulladdr=("http://"+IPAddr+":"+str(port))
    l6=ctk.CTkLabel(master=w, text="Share Link (Copy - Ctrl+C)",text_color="#3498DB",font=('Century Gothic',30))
    link = ctk.CTkTextbox(master=w, width=200,height=20)
    link.insert("0.5",fulladdr)
    link.configure(state='disabled')
    closebutton = ctk.CTkButton( 
        master=w,                   
	    text = 'Close Server', 
	    fg_color = '#F1C40F', 
	    text_color = '#000',
	    hover_color = '#AA0',
	    command = serverclose
    )
    l1.pack()
    l2.pack(padx=15,pady=15)
    l3.pack()
    l4.pack(padx=15,pady=15)
    l5.pack()
    l6.pack(padx=15,pady=15)
    link.pack()
    closebutton.pack(padx=15,pady=15)
    w.mainloop()
    
    
bgim=ctk.CTkImage(Image.open(r"D:\Python\pattern.png"),
                  size=(1366,768)
                  )  
bg=ctk.CTkLabel(master=app,image=bgim)

frame=ctk.CTkFrame(master=bg,width=1000,height=1000,corner_radius=15)
frame.place(relx=0.5,rely=0.5,anchor=ctk.CENTER)

fgim=ctk.CTkImage(Image.open(r"D:\Python\fg.jpg"),
                  size=(200,200))  
fg=ctk.CTkLabel(master=frame,
            image=fgim
            )    
fg.pack()
im=ctk.CTkImage(
	Image.open(r"D:\Python\folder.png"),
 	size=(35,35)
)
follabel=ctk.CTkLabel(
    master=frame,
    text="Browse Folder", 
    font=("Arial",15),
    fg_color="transparent",
    text_color="#D1F2EB",
    
)
portlabel=ctk.CTkLabel(
    master=frame,
    text="Insert Port", 
    font=("Arial",15),
    fg_color="transparent",
    text_color="#D1F2EB",
)
portbox=ctk.CTkEntry(
    master=frame,
    placeholder_text="Default: 9999",
    width=185,
    height=42,
    border_width=2,
    corner_radius=8
)
button = ctk.CTkButton( 
    master=frame,                   
	image=im,
	text = 'Browse', 
	fg_color = '#F1C40F', 
	text_color = '#000',
	hover_color = '#AA0',
	command = hshare
 )

button2 = ctk.CTkButton( 
    master=frame,                   
	text = 'Start Server', 
	fg_color = '#48C9B0', 
	text_color = '#000',
	hover_color = '#2E86C1',
	command = serve
 )
flab= ctk.CTkLabel (
        master=frame,
        text=" ",
        font=("Arial",15),
        fg_color="transparent",
        text_color="#D1F2EB",
    )
bg.pack()
follabel.pack()
button.pack()
portlabel.pack()
portbox.pack()    
button2.pack(padx=20,pady=20)
#run
app.mainloop()
os.system("taskkill /F /im python.exe") #if App Closed Using Close(x) Button, This will terminate the http server
