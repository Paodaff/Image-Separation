__author__ = 'Mira Gleizer'

import MyChangePic as myC
import cv2
import Tkinter as tk
from PIL import Image
import tkFileDialog
from tkinter import messagebox as mb
import os
import funfiles as ff
###################################################################

global Isinit
Isinit=0

root = tk.Tk()
root.geometry('1200x850+300+150')
root.title('Matala Bonus by Mira Gleizer')
bg = Image.open('bg1.gif')
bg = tk.PhotoImage(file='bg1.gif')
labelbg = tk.Label(root)
labelbg.configure(image=bg)
labelbg.place(x=0, y=0, relwidth=1, relheight=1)
root.resizable(width=True, height=True)
f_top = tk.LabelFrame(bg='black')
f_bot = tk.LabelFrame()

f_top.grid(row=0, column=0)
f_bot.grid(row=1, column=0, pady=10)

def init():

    global f_left
    global f_right
    global f_bot_right1

    global f_bot_right2
    global Llabel
    global labels
    global labelsR1
    global labelsR2
    global Isinit

    if Isinit == 1:
        f_right = tk.LabelFrame(f_bot, text='Results', font=('Comic Sans MS', 18, 'bold'))
        f_right.grid(row=0, column=1, padx=20, pady=10)
        labels = []
        r = 0
        c = 0
        for j in range(21):
            label = tk.Label(f_right)
            label.grid(row=r, column=c)
            labels.append(label)
            c = c + 1
            if c > 4:
                c = c - 5
                r = r + 1
        f_bot_right1 = tk.LabelFrame(f_right, text=' Blend of Red Images')
        f_bot_right1.grid(row=5, column=0)
        f_bot_right2 = tk.LabelFrame(f_right, text='Not Listed Image ')
        f_bot_right2.grid(row=5, column=1)
        labelsR1 = tk.Label(f_bot_right1)
        labelsR1.grid()
        labelsR2 = tk.Label(f_bot_right2)
        labelsR2.grid()

        Isinit = 2

    if Isinit == 0:
        f_left = tk.LabelFrame(f_bot, text='Original Image', font=('Comic Sans MS', 18, 'bold'))
        f_left.grid(row=0, column=0, padx=20, pady=10)
        Llabel = tk.Label(f_left)
        Llabel.grid(row=0, column=0, padx=20, pady=10)
        Isinit = 1

def openfn():
    filename = tkFileDialog.askopenfilename(title='Select file')
    return filename


def check_deletefn(myfile):
    # if file exist - delete it
    if os.path.isfile(myfile):
        os.remove(myfile)
    else:
        pass


def close():
    # deleting working files
    check_deletefn('original.gif')
    check_deletefn('original.png')
    check_deletefn('finalimage.png')
    check_deletefn('myImage.png')
    check_deletefn('myImage.gif')
    check_deletefn('myimg.png')
    check_deletefn('my.gif')
    #close main window
    root.destroy()
    root.quit()


def open_img(event):
    global x

    x = openfn()
    if x:
        init()
        image = Image.open(x)
        img = cv2.imread(x)
        img = image.resize((500, 500), Image.ANTIALIAS)
        img.save('original.gif')
        img = tk.PhotoImage(file='original.gif')
        image.save('original.png')
        Llabel.configure(image=img, padx=20, pady=20)
        Llabel.image = img  # keep a reference!
        Llabel.grid()

def add_contr(event):

    global x
    image = myC.addContast(x)
    cv2.imwrite('original.png', image)
    x = 'original.png'
    image = Image.open(x)
    img = cv2.imread(x)
    img = image.resize((500, 500), Image.ANTIALIAS)
    img.save('original.gif')
    img = tk.PhotoImage(file='original.gif')
    image.save('original.png')
    Llabel.configure(image=img, padx=20, pady=20)
    Llabel.image = img  # keep a reference!
    Llabel.grid()

def find_cor(event):
    global x

    if os.path.isfile('original.png'):

        ff.PicToArr(x)
        finalImg, fNames = myC.FindPic(x)
        fNames.remove(x)
        init()
        i = 0
        r = 0
        c = 0
        for item in fNames:

            image = Image.open(item)
            img = image.resize((100, 100), Image.ANTIALIAS)
            img.save('my.gif')
            img = tk.PhotoImage(file='my.gif')
            if i < 20 :
                labels[i].configure(image=img)
                labels[i].image = img  # keep a reference!
                labels[i].grid(row=r, column=c)
                i = i + 1
                c = c + 1
                if c > 4:
                    c = c - 5
                    r = r + 1
            elif i == 20:
                labelsR2.configure(image=img)
                labelsR2.image = img  # keep a reference!
                labelsR2.grid(row=r, column=1)
                i = i + 1
            elif i == 21:
                labelsR1.configure(image=img)
                labelsR1.image = img  # keep a reference!
                labelsR1.grid(row=r, column=0)
                i = i + 1



c = tk.Canvas(f_top, width=1190, height=60, bg='black')
c.pack()

menuBtn1 = c.create_rectangle(110, 10, 200, 40, tag='menuBtn1', fill='#C2B6BF', outline='#836d7e', width=3)
b1line1 = c.create_line(110, 10, 110, 40, fill='#ede9ec', width=3)
b1line2 = c.create_line(110, 10, 200, 10, fill='#ede9ec', width=3)
mylabel1 = c.create_text((160, 25), tag='menuBtn1', text='Open image')

menuBtn2 = c.create_rectangle(510, 10, 600, 40, tag='menuBtn2', fill='#C2B6BF', outline='#836d7e', width=3)
b2line1 = c.create_line(510, 10, 510, 40, fill='#ede9ec', width=3)
b2line2 = c.create_line(510, 10, 600, 10, fill='#ede9ec', width=3)
mylabel2 = c.create_text((560, 25), tag='menuBtn2', text='Add contrast')

menuBtn2 = c.create_rectangle(895, 10, 985, 40, tag='menuBtn3', fill='#C2B6BF', outline='#836d7e', width=3)
b2line1 = c.create_line(895, 10, 895, 40, fill='#ede9ec', width=3)
b2line2 = c.create_line(895, 10, 985, 10, fill='#ede9ec', width=3)
mylabel2 = c.create_text((940, 25), tag='menuBtn3', text='Decompose')

c.tag_bind('menuBtn1', '<Button-1>', open_img)
c.tag_bind('menuBtn2', '<Button-1>', add_contr)
c.tag_bind('menuBtn3', '<Button-1>', find_cor)


def motion_b1():
    #Animation
    c.move(menuBtn1, 2, 0)
    c.move(b1line1, 2, 0)
    c.move(b1line2, 2, 0)
    c.move(mylabel1, 2, 0)

    c.move(menuBtn2, -2, 0)
    c.move(b2line1, -2, 0)
    c.move(b2line2, -2, 0)
    c.move(mylabel2, -2, 0)
    if c.coords(menuBtn1)[2] < 450:
        root.after(1, motion_b1)


motion_b1()

root.protocol('WM_DELETE_WINDOW', close)
root.mainloop()
