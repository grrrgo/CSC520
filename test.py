from tkinter import *
import random

root = Tk()


listOfCards = [i for i in range(8)]+[i for i in range(8)]
random.shuffle(listOfCards)
listOfCards = [listOfCards[x:x+4] for x in range(0, 16, 4)]
print(listOfCards)

matrix = {}
shown = []
click = 0
back = PhotoImage(file='./back.gif')
blank = PhotoImage(file='./blank.gif')


def callback(event):
    card = event.widget
    if len(shown) == 0:
        shown.append(card)
        pic = PhotoImage(file='./' + card.file + '.gif')
        card.configure(image=pic)
        card.pic = pic
        card.show = True
    elif len(shown) == 1:
        if shown[0].file == card.file:
            card.configure(image=blank)
            matrix[shown[0].position].configure(image=blank)
            del shown[0]
        else:
            shown.append(card)
            pic = PhotoImage(file='./' + card.file + '.gif')
            card.configure(image=pic)
            card.pic = pic
            card.show = True
    elif len(shown) == 2:
        if card.file == shown[0].file:
            card.configure(image=blank)
            matrix[shown[0].position].configure(image=blank)
            del shown[0]
        elif card.file == shown[1].file:
            card.configure(image=blank)
            matrix[shown[1].position].configure(image=blank)
            del shown[1]
        else:
            shown.append(card)
            matrix[shown[0].position].configure(image=back)
            del shown[0]
            pic = PhotoImage(file='./' + card.file + '.gif')
            card.configure(image=pic)
            card.pic = pic
            card.show = True

for r in range(4):
    for c in range(4):
        position = str(r) + str(c)
        # photo = PhotoImage(file='./'+str(listOfCards[r][c])+'.gif')
        matrix[position] = Label(root, image=back, borderwidth=2)
        matrix[position].position = position
        matrix[position].photo = back
        matrix[position].file = str(listOfCards[r][c])
        matrix[position].show = False
        matrix[position].bind("<Button-1>", callback)
        matrix[position].grid(row=r, column=c)

root.mainloop()
