from tkinter import *
from PIL import ImageTk,Image
import random

parent=Tk()
parent.geometry('300x300')
parent.title('dice')
Blankline = Label(parent,text='fare play')
dice = ['dice1.png', 'dice2.png', 'dice3.png', 'dice4.png', 'dice5.png', 'dice6.png']
diceImages = ImageTk.PhotoImage(Image.open(random.choice(dice)))

ImageLable = Label(parent, image=diceImages)

ImageLable.image = diceImages
ImageLable.pack(expand = True)



def rolling_dice():
    diceImages = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    ImageLable.configure(image=diceImages)
    ImageLable.image=diceImages

roll2=Button(parent,text='roll the dice ', command =rolling_dice)
roll2.pack()
parent.mainloop()



