#import libararies
import tkinter
from tkinter import *
import socket
import _thread
import time
from functools import partial

#start the program
win=0
lost=0
client=0
buttonclicked=False
colors=['brown','orange','red','purple','blue','pink','black','green','gray','yellow']

def check(color):
    global win
    global lost
    if(color==colorlabel['fg']):
        win+=1
        wonlabel['text']='won: '+str(win)
    else:
        lost+=1
        loselabel['text']='lost: '+str(lost)
    global buttonclicked
    buttonclicked= True
    reset()
    
def reset():
    client.send('x'.encode('ascii'))
    
def socketCreation():
    c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host='127.0.0.1'
    port=7002
    c.connect((host,port))
    global client 
    client=c
    global livesremaining
    while True:
        msg=c.recv(2048).decode('ascii')
        for color in colors:
            if(color[0]==msg[0]):
                colorlabel['text']=color
            if(color[0]==msg[1]):
                colorlabel['fg']=color
        for i in range(10,0,-1):
            timer['text']='time: '+str(i)
            global buttonclicked
            if(buttonclicked):
                buttonclicked=False
                break
            time.sleep(1)
        reset()
#window
window=tkinter.Tk()
window.title=('color game')
window['bg']='white'

#instructions
instruction=tkinter.Label(window,text='choose the color of word , not the word itself',bg='yellow',fg='black',font=('TimesNewRoman',20))
instruction.grid(column=1,row=1,padx=5,pady=5)

#win label
wonlabel=tkinter.Label(window,text='won: '+str(win),bg='white',fg='green',font=('TimesNewRoman',20))
wonlabel.grid(column=1,row=2)

#lose label
loselabel=tkinter.Label(window,text='lost: '+str(lost),bg='white',fg='red',font=('TimesNewRoman',20))
loselabel.grid(column=1,row=3)

#timer
timer=tkinter.Label(window,text='time: 10',font=('TimesNewRoman',15))
timer.grid(column=1,row=5,padx=5,pady=5)

#colors
colorlabel=tkinter.Label(window,text=" ",font=('TimesNewRoman',20))
colorlabel.grid(column=4,row=5,padx=5,pady=5)

#buttons
#red button
redbutton=tkinter.Button(window,bg='red',width=7,height =3,command=partial(check,'red'))
redbutton.grid(column=2,row=6,padx=6,pady=6)
#orange button
orangebutton=tkinter.Button(window,bg='orange',width=7,height=3,command=partial(check,'orange'))
orangebutton.grid(column=3,row=6,padx=6,pady=6)
#green button
greenbutton=tkinter.Button(window,bg='green',width=7,height=3,command=partial(check,'green'))
greenbutton.grid(column=4,row=6,padx=6,pady=6)
#blue button
bluebutton=tkinter.Button(window,bg='blue',width=7,height=3,command=partial(check,'blue'))
bluebutton.grid(column=5,row=6,padx=6,pady=6)
#yellow button
yellowbutton=tkinter.Button(window,bg='yellow',width=7,height=3,command=partial(check,'yellow'))
yellowbutton.grid(column=6,row=6,padx=6,pady=6)
#purple button
purplebutton=tkinter.Button(window,bg='purple',width=7,height=3,command=partial(check,'purple'))
purplebutton.grid(column=2,row=8,padx=6,pady=6)
#pink button
pinkbutton=tkinter.Button(window,bg='pink',width=7,height=3,command=partial(check,'pink'))
pinkbutton.grid(column=3,row=8,padx=6,pady=6)
#brown button
brownbutton=tkinter.Button(window,bg='brown',width=7,height=3,command=partial(check,'brown'))
brownbutton.grid(column=4,row=8,padx=6,pady=6)
#black button
blackbutton=tkinter.Button(window,bg='black',width=7,height=3,command=partial(check,'black'))
blackbutton.grid(column=5,row=8,padx=6,pady=6)
#gray button
graybutton=tkinter.Button(window,bg='gray',width=7,height=3,command=partial(check,'gray'))
graybutton.grid(column=6,row=8,padx=6,pady=6)

#start the window
_thread.start_new_thread(socketCreation,())
window.mainloop()
