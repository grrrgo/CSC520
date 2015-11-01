## =============================
## main.py
## authors:
##           Chen Zhang
##           Deepika Vinodkumar
##           Deesha Shingadia
##           Tejaswini Koduru
##           Megha Dhoke
##           Chunhua Yang
##           Kalyan Kumar Yalagandula
## date: Nov. 1st 2015
## version: 1
## class: Python Fall 2015, Dr. Riehle


from tkinter import *
from tkinter import messagebox
import random
import constants
try:
    import winsound

    def play():
        winsound.PlaySound("song.wav", winsound.SND_FILENAME)
except ImportError:
    import os

    def play():
        os.system("afplay ./song.wav &")


class Game:
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("Game")
        self.listOfCards = [i for i in range(8)]+[i for i in range(8)]
        random.shuffle(self.listOfCards)
        self.listOfCards = [self.listOfCards[x:x+4] for x in range(0, 16, 4)]
        print(self.listOfCards)
        self.matrix = {}
        self.shown = []
        self.click = 0
        self.numberLeft = 8
        self.sec = 30
        self.done = False
        self.back = PhotoImage(data=constants.back)
        self.blank = PhotoImage(data=constants.blank)
        for r in range(4):
            for c in range(4):
                position = str(r) + str(c)
                # photo = PhotoImage(file='./'+str(self.listOfCards[r][c])+'.gif')
                self.matrix[position] = Label(self.root, image=self.back, borderwidth=2)
                self.matrix[position].photo = self.back
                self.matrix[position].position = position
                self.matrix[position].file = str(self.listOfCards[r][c])
                self.matrix[position].show = False
                self.matrix[position].bind("<Button-1>", self.callback)
                self.matrix[position].grid(row=r, column=c)

        Label(self.root, text='Time Left:').grid(row=6, column=1, columnspan=2)
        self.time = Label(self.root, text='time')
        self.time.grid(row=6, column=2, columnspan=2)
        self.root.withdraw()
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry("+%d+%d" % (x, y))
        self.root.deiconify()
        self.tick()
        self.root.mainloop()

    def callback(self, event):
        card = event.widget
        print(card)
        if card.show:
            return
        
        if len(self.shown) == 0:
            self.shown.append(card)
            pic = PhotoImage(file='./imgs/' + card.file + '.gif')
            card.configure(image=pic)
            card.pic = pic
            card.show = True
            
        elif len(self.shown) == 1:
        
            if self.shown[0].file == card.file:
                self.numberLeft -= 1

                def handle():
                    card.configure(image=self.blank)
                    card.show = True
                    self.matrix[self.shown[0].position].configure(image=self.blank)
                    self.matrix[self.shown[0].position].show = True
                    del self.shown[0]
                    play()

                pic = PhotoImage(file='./imgs/' + card.file + '.gif')
                card.configure(image=pic)
                card.pic = pic
                card.show = True
                card.after(300, handle)

            else:
                self.shown.append(card)
                pic = PhotoImage(file='./imgs/' + card.file + '.gif')
                self.matrix[self.shown[0].position].show = True
                card.configure(image=pic)
                card.pic = pic
                card.show = True

        elif len(self.shown) == 2:
            if card.file == self.shown[0].file:
                self.numberLeft -= 1

                def handle():
                    card.configure(image=self.blank)
                    card.show = True
                    self.matrix[self.shown[0].position].configure(image=self.blank)
                    self.matrix[self.shown[0].position].show = True
                    del self.shown[0]
                    play()

                pic = PhotoImage(file='./imgs/' + card.file + '.gif')
                card.configure(image=pic)
                card.pic = pic
                card.show = True
                card.after(300, handle)
                
            elif card.file == self.shown[1].file:
                self.numberLeft -= 1

                def handle():
                    card.configure(image=self.blank)
                    card.show = True
                    self.matrix[self.shown[1].position].configure(image=self.blank)
                    self.matrix[self.shown[1].position].show = True
                    del self.shown[1]
                    play()

                pic = PhotoImage(file='./imgs/' + card.file + '.gif')
                card.configure(image=pic)
                card.pic = pic
                card.show = True
                card.after(300, handle)

            else:
                self.shown.append(card)
                self.matrix[self.shown[0].position].configure(image=self.back)
                self.matrix[self.shown[0].position].show = False
                del self.shown[0]
                pic = PhotoImage(file='./imgs/' + card.file + '.gif')
                card.configure(image=pic)
                card.pic = pic
                card.show = True
                
        self.isDone()

    def isDone(self):
        if self.numberLeft == 0:
            self.done = True
            isPlayAgain= messagebox.askyesno("Game", "Congrats! You won! Do You want to play again?")
            self.playAgain(isPlayAgain)

    def tick(self):
        if not self.done:
            if self.sec != 0:
                self.sec -= 1
                self.time['text'] = self.sec
                self.time.after(1000, self.tick)
            else:
                isPlayAgain= messagebox.askyesno("Game", "Times up! Do You want to play again?")
                self.playAgain(isPlayAgain)
        else:
            return

    def playAgain(self, isPlayAgain):
        if isPlayAgain:
            self.root.destroy()
            game = Game()
        else:
            self.root.destroy()

game = Game()
