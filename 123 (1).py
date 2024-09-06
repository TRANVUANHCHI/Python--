import tkinter
import pygame

cx=0
cy=200
px = 400
py = 500

kx=400
ky=200

tensu = 0

x_houkou1 = 1
y_houkou1 = 1
x_houkou2 = 1



def teki1move():
    global cx, cy, kx, ky, x_houkou1, y_houkou1, x_houkou2, tensu

    if cx -(img1.width()/2)<= 0:
        x_houkou1 = 1
    elif cx +(img1.width()/2)>= 800:
        x_houkou1 = -1

    if cy -(img1.height()/2)<= 0:
        y_houkou1 = 1
    elif cy +(img1.height()/2)>= 600:
        music1.stop()
        return
        y_houkou1 = -1

    if atari("TORI1", "PAD1"):
        if y_houkou1==1:
            y_houkou1 = -1
            tensu = tensu + 1
            label1.configure(text=tensu)
            sound.play()

    if tensu >= 3:
        canvas.coords("KABE1", kx, ky)
    if kx - (img3.width()/2) <= 0:
        x_houkou2 = 1
    elif kx + (img3.width()/2) >= 800:
        x_houkou2 = -1
    kx = kx + 2 * x_houkou2


    cx = cx + 5 * x_houkou1
    cy = cy + 5 * y_houkou1

    canvas.coords("TORI1", cx, cy)
    root.after(10, teki1move)

def pad1move(event):
    global px, py
    px = event.x
    canvas.coords("PAD1", px, py)

def atari(ID1, ID2):
    cxl = canvas.bbox(ID1)[0]
    cxr = canvas.bbox(ID1)[2]
    cyt = canvas.bbox(ID1)[1]
    cyb = canvas.bbox(ID1)[3]

    pxl = canvas.bbox(ID2)[0]
    pxr = canvas.bbox(ID2)[2]
    pyt = canvas.bbox(ID2)[1]
    pyb = canvas.bbox(ID2)[3]

    if cxr > pxl:
        if cxl < pxr:
            if cyb > pyt:
                if cyt < pyb:
                    return True
    return False

root = tkinter.Tk()
canvas = tkinter.Canvas(width=800,height=600)
canvas.pack()

img0 = tkinter.PhotoImage(file = "R.png")
img1 = tkinter.PhotoImage(file = "TORI.png")
img2 = tkinter.PhotoImage(file = "paddle.png")
img3 = tkinter.PhotoImage(file="sun.png")

canvas.create_image(400, 300, image=img0, tag="BAK")
canvas.create_image(cx,cy, image=img1, tag="TORI1")
canvas.create_image(px,py, image=img2, tag="PAD1")
canvas.create_image(kx-800, ky, image=img3, tag="KABE1" )

label1 = tkinter .Label(root, text=tensu, font=("Times","20"))
label1.place(x=730, y=20)
label2 = tkinter .Label(root, text="TRANVUANHCHI", font=("Times","20"))
label2.place(x=580, y=60)


pygame.init()
sound = pygame.mixer.Sound("maou_se_onepoint31.mp3")

music1 = pygame.mixer.music
music1.load ("maou_game_vehicle03.mp3")
music1.set_volume(0.5)
music1.play (-1)

teki1move()
canvas.bind('<Motion>', pad1move)
root.mainloop()
