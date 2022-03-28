from tkinter import *
from PIL import Image,ImageTk
from pygame import mixer
mixer.init()

window = Tk()
window.geometry("890x400")
window.title("Hải App")
background = Image.open('ngan.jpg')
background = background.resize((280,404))
background_load = ImageTk.PhotoImage(background)

hai5 = Image.open("hai1.jpg")
hai5 = hai5.resize((389,400))
hai_load5 = ImageTk.PhotoImage(hai5)
hai_screen5 = Label(window,image = hai_load5)
hai_screen5.place(x=570,y=0)

def submit():
    if listbox.get(listbox.curselection()) == "Chào Hải nhá":
        file = "chao.ogg"
        mixer.music.load(file)
        mixer.music.play(loops=0)
    elif listbox.get(listbox.curselection()) == "Em sắp thi rồi nè huhu":
        file = "thi.ogg"
        mixer.music.load(file)
        mixer.music.play(loops=0)
    elif listbox.get(listbox.curselection()) == "Hải đi giáng sinh không":
        file = "giangsinh_1.ogg"
        mixer.music.load(file)
        mixer.music.play(loops=0)
    elif listbox.get(listbox.curselection()) == "Hải Yêu Ngân Không":
        file = "yeu.ogg"
        mixer.music.load(file)
        mixer.music.play(loops=0)
    elif listbox.get(listbox.curselection()) == "Hải thấy Ngân xinh không?":
        file = "dep.ogg"
        mixer.music.load(file)
        mixer.music.play(loops=0)
    else:
        pass

background_screen = Label(window,image=background_load).place(x=0,y=0) 
listbox = Listbox(window,font = ("Arial",21),width=20,height=20) 
listbox.pack(anchor=CENTER,pady=0)

listbox.insert(1,"Chào Hải nhá")
listbox.insert(2,"Em sắp thi rồi nè huhu")
listbox.insert(3,"Hải đi giáng sinh không")
listbox.insert(4,"Hải Yêu Ngân Không")
listbox.insert(5,"Hải thấy Ngân xinh không?")

submit_button = Button(window,text="submit",command=submit)
submit_button.place(x= 420,y=300)

window.mainloop()
