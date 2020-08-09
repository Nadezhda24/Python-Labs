import socket
from tkinter import *
import tkinter as tk

def click_send():
    sock.send(text_record.get().encode())
    text.insert(1.0,sock.recv(1024).decode() + "\n")
    text_record.delete(0, tk.END)

window = Tk()
window.title("Чат")
window.geometry('500x600')
window["bg"] = "lavender"
frame = Frame(window)
frame["bg"] = "lavender"
frame.pack()
sock = socket.socket()
sock.connect(("localhost", 9090))
str_record = StringVar()
text_record = Entry(frame, font=("Comic Sans MS", 10), textvariable = str_record,width=45)
text_record.grid(row=0, column=0)
send = Button(frame, text="Отправить", background="light steel blue", foreground="RoyalBlue4", padx="20", pady="8", font=("Comic Sans MS", 8),command=lambda: click_send())
send.grid(row=0, column=1)
text = Text(frame, width=45, height=32,  wrap=WORD)
text.grid(row=1)
window.mainloop()
sock.close()