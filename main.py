from tkinter import *
import random

root = Tk()
root.title("Виселица")

canvas = Canvas(root, width=600, height=600)
canvas.pack()

def but():
    y = 0
    while y < 600:
        x = 0
        while x < 600:
            canvas.create_rectangle(x, y, x+33, y+27, fill="white", outline="blue")
            x = x+33
        y = y+27


faq = '''Привет, Забубень! 
Ты меня слышишь?
'''
canvas.create_text(310, 240, text=faq, fill="purple", font=("Helvetica", "14"))
slova = ["виселица", "смартфон", "маргарин", "мегагерц", "страница", "креветка", "микрофон"]

def arr():
    but()
    word = random.choice(slova)
    wo = word[1: -1]
    wor = []
    for i in wo:
        wor.append(i)
    a0 = canvas.create_text(282, 40, text=word[0], fill="purple", font=("Helvetica", "18"))
    a1 = canvas.create_text(315, 40, text="_", fill="purple", font=("Helvetica", "18"))
    a2 = canvas.create_text(347, 40, text="_", fill="purple", font=("Helvetica", "18"))
    a3 = canvas.create_text(380, 40, text="_", fill="purple", font=("Helvetica", "18"))
    a4 = canvas.create_text(412, 40, text="_", fill="purple", font=("Helvetica", "18"))
    a5 = canvas.create_text(444, 40, text="_", fill="purple", font=("Helvetica", "18"))
    a6 = canvas.create_text(477, 40, text="_", fill="purple", font=("Helvetica", "18"))
    a7 = canvas.create_text(510, 40, text=word[-1], fill="purple", font=("Helvetica", "18"))
    list = [1, 2, 3, 4, 5, 6]
    alfabet = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя"
    er = []
    win = []

    def a(v):
        ind_alf = alfabet.index(v)
        key = alfabet[ind_alf]

        if v in wor:
            ind = wor.index(v)
            b2 = list[ind]
            wor[ind] = '1'

            def kord():
                if b2 == 1:
                    x1, y1 = 315, 40
                if b2 == 2:
                    x1, y1 = 347, 40
                if b2 == 3:
                    x1, y1 = 380, 40
                if b2 == 4:
                    x1, y1 = 412, 40
                if b2 == 5:
                    x1, y1 = 444, 40
                if b2 == 6:
                    x1, y1 = 477, 40
                return x1, y1

            x1, y1 = kord()
            win.append(v)
            a2 = canvas.create_text(x1, y1, text=word2[ind], fill="purple", font=("Helvetica", "18"))
            btn[key]["bg"] = "green"

            if not v in wor:
                btn[key]["state"] = "disabled"
            if v in wor:
                win.append(v)
                ind2 = wor.index(v)
                b2 = list1[ind2]
                x1, y1 = kord()
                canvas.create_text(x1, y1, text=wo[ind2], fill="purple", font=("Helvetica", "18"))
            if len(win) == 6:
                canvas.create_text(150, 150, text="Ты победил!", fill="purple", font=("Helvetica", "18"))
                for i in alfabet:
                    btn[i]["state"] = "disabled"
        else:
            er.append(v)
            btn[key]["bg"] = "red"
            btn[key]["state"] = "disabled"

            if len(er) == 1:
                golova()
            elif len(er) == 2:
                telo()
            elif len(er) == 3:
                rukaL()
            elif len(er) == 4:
                rukaP()
            elif len(er) == 5:
                nogaL()
            elif len(er) == 6:
                nogaP()
                end()
    btn = {}

    def gen(u, x, y):
        btn[u] = Button(root, text=u, width=3, height=1, command=lambda: a(u))
        btn[u].place(x=str(x), y=str(y))

        x = 265
        y = 110
        for i in alfabet[0:8]:
            gen(i, x, y)
            x = x+33
        x = 265
        y = 137
        for i in alfabet[8:16]:
            gen(i, x, y)
            x = x+33
        x = 265
        y = 164
        for i in alfabet[16:24]:
            gen(i, x, y)
            x = x+33
        x = 265
        y = 191
        for i in alfabet[24:33]:
            gen(i, x, y)
            x = x+33

    def golova():
        canvas.create_oval(79, 59, 120, 80, width=4, fill="white")
        root.update()

    def telo():
        canvas.create_line(100, 80, 100, 200, width=4, fill="white")
        root.update()

    def rukaP():
        canvas.create_line(100, 80, 145, 100, width=4, fill="white")
        root.update()

    def rukaL():
        canvas.create_line(100, 80, 45, 100, width=4, fill="white")
        root.update()

    def nogaL():
        canvas.create_line(100, 200, 45, 300, width=4, fill="white")
        root.update()

    def nogaP():
        canvas.create_line(100, 200, 145, 300, width=4, fill="white")
        root.update()

    def end():
        canvas.create_text(150, 150, text="Ты проиграл", fill="purple", font=("Helvetica", "18"))
        for i in alfabet:
            btn[i]["state"] = "disabled"


btn01 = Button(root, text="Начать!", width=10, height=1, command=lambda: arr())
btn01.place(x=258, y=542)
btn01["bg"] = "red"



root.mainloop()
