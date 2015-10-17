from tkinter import *
from tkinter import messagebox
import random

root = Tk()


listOfCards = [i for i in range(8)]+[i for i in range(8)]
random.shuffle(listOfCards)
listOfCards = [listOfCards[x:x+4] for x in range(0, 16, 4)]
print(listOfCards)

matrix = {}
shown = []
click = 0
numberLeft = 8
sec = 30
back = PhotoImage(file='./back.gif')
blank = PhotoImage(file='./blank.gif')


def callback(event):
    global numberLeft
    card = event.widget
    if card.show:
        return
    if len(shown) == 0:
        shown.append(card)
        pic = PhotoImage(file='./' + card.file + '.gif')
        card.configure(image=pic)
        card.pic = pic
        card.show = True
    elif len(shown) == 1:
        if shown[0].file == card.file:
            card.configure(image=blank)
            numberLeft -= 1
            card.show = True
            matrix[shown[0].position].configure(image=blank)
            matrix[shown[0].position].show = True
            del shown[0]
        else:
            shown.append(card)
            pic = PhotoImage(file='./' + card.file + '.gif')
            matrix[shown[0].position].show = True
            card.configure(image=pic)
            card.pic = pic
            card.show = True
    elif len(shown) == 2:
        if card.file == shown[0].file:
            card.configure(image=blank)
            numberLeft -= 1
            card.show = True
            matrix[shown[0].position].configure(image=blank)
            matrix[shown[0].position].show = True
            del shown[0]
        elif card.file == shown[1].file:
            card.configure(image=blank)
            numberLeft -= 1
            card.show = True
            matrix[shown[1].position].configure(image=blank)
            matrix[shown[1].position].show = True
            del shown[1]
        else:
            shown.append(card)
            matrix[shown[0].position].configure(image=back)
            matrix[shown[0].position].show = False
            del shown[0]
            pic = PhotoImage(file='./' + card.file + '.gif')
            card.configure(image=pic)
            card.pic = pic
            card.show = True
    isDone()


def isDone():
    global numberLeft
    if numberLeft == 0:
        messagebox.showinfo("info", "Congrats! You won!")
        root.destroy()


def tick():
    global sec
    if sec != 0:
        sec -= 1
        time['text'] = sec
        time.after(1000, tick)
    else:
        messagebox.showinfo("info", "Times up!")
        root.destroy()

for r in range(4):
    for c in range(4):
        position = str(r) + str(c)
        photo = PhotoImage(file='./'+str(listOfCards[r][c])+'.gif')
        matrix[position] = Label(root, image=back, borderwidth=2)
        matrix[position].position = position
        matrix[position].photo = back
        matrix[position].file = str(listOfCards[r][c])
        matrix[position].show = False
        matrix[position].bind("<Button-1>", callback)
        matrix[position].grid(row=r, column=c)

Label(root, text='Time Left:').grid(row=5, column=1,columnspan=2)
time = Label(root, text='time')
time.grid(row=5, column=2, columnspan=2)
tick()
root.mainloop()

