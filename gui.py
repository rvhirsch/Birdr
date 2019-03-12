#Run with: python gui.py

from Tkinter import *
import tkMessageBox

from Parker_Birder import *

# set up bird info
birds = makedict("birds.txt")
yesbirds = set()
nobirds = set()

def onchoice():
    global birds
    global yesbirds
    global nobirds

    bird = getrandombird(birds)
    while (bird in yesbirds or bird in nobirds): # make sure bird not seen yet
        bird = getrandombird(birds)

    messageVar.configure(text = bird)
    return bird

def yesvote():
    global bird
    yesbirds.add(bird)
    print(yesbirds)

    summary = getwikisummary(bird)
    tkMessageBox.showinfo(bird + " Summary", summary)

    bird = onchoice()
    return yesbirds

def novote():
    global bird
    nobirds.add(bird)
    print(nobirds)

    bird = onchoice()
    return nobirds

def getstats():
    global yesbirds
    global nobirds

    string = "Liked:" + ", ".join(list(yesbirds))
    string += "\nDisliked: " + ", ".join(list(nobirds))

    tkMessageBox.showinfo("Your Stats", string)

    print(string)
    return string

master = Tk()
master.title("BIRDR")

ht = 400
wt = 600
w = Canvas(master, width=wt, height=ht)
w.pack_propagate(0)

frame = Frame(master)
frame.pack(side = BOTTOM)

# set up swipe buttons
nobutton = Button(frame, text = 'X', fg ='red', command=novote)
nobutton.pack( side = LEFT )

yesbutton = Button(frame, text = '<3', fg ='green', command=yesvote)
yesbutton.pack( side = RIGHT)

statsbutton = Button(frame, text = 'GET STATS', fg ='blue', command=getstats)
statsbutton.pack( side = BOTTOM )

# see bird name
bird = getrandombird(birds)
messageVar = Message(master, text = bird, padx=250, pady=200)
messageVar.config(bg='lightgreen')
messageVar.pack(side = TOP)

# w.pack()

mainloop()
