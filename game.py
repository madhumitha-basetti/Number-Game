from tkinter import *
from tkinter import messagebox
import random
import time
import turtle
window=Tk()
window.geometry('300x300')
window.title('Game')
num=StringVar()
label3=Label(window,text='Number Sequence Memory Game',bg='white',fg='blue',relief='solid',font=('arial',30,'bold')).pack()
label=Label(window,text='Number',bg='pink',fg='blue',font=('arial',30,'bold'))
label.place(x=100,y=350)
l=[]
for i in range(10):
    x=random.randint(0,9)
    l.append(x)
print(l)
def start():
    entry = Entry(window, textvariable=num, font=('arial', 30, 'bold'))
    entry.place(x=400, y=350)
    button = Button(window, text='Result', bg='blue', fg='orange', relief='solid',font=('arial', 30, 'bold'), command=quit).place(x=300,
                                                                                                                 y=500)
def t():
    s=turtle.Turtle()
    m=turtle.Screen()
    for i in range(10):
        s.write(l[i],font=('Arial',60,'normal'))
        time.sleep(2)
        s.reset()
        s.write('|',font=('Arial',60,'normal'))
        time.sleep(0.5)
        s.write('|',font=('italic',60,'normal'))
        s.reset()
    m.bye()
buttont=Button(window, text='Start Game', bg='brown', fg='white',relief='solid', font=('arial', 30, 'bold'), command=t).place(x=100,
                                                                                                                 y=100)

def quit():
    a = ''
    for i in range(10):
        a = a + str(l[i])
    print(a)
    print(num.get())
    if num.get()==a:
        messagebox.showinfo('showinfo','Hey,Congrats! You Won')
    else:
        messagebox.showinfo('showinfo','Sorry! You Lost. Better Luck next time!')
    exit()

button=Button(window,text='Input',bg='green',fg='yellow',relief='solid',font=('arial',30,'bold'),command=start).place(x=100,y=200)
window.mainloop()
