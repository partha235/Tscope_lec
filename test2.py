import turtle as t  # import library
from time import sleep
# screen=t.Screen()
# print(screen)
# screen._root.geometry("+200+200")
t.speed(1) # pen speed.
t.setup(width=1000, height=600) # declaring windows size
print(t.pos()) # pen position
t.penup
t.setpos(-250,0) 
t.pendown()
t.fd(15)

# create two turtle
l1=t.Turtle()
l2=t.Turtle()

l1.pencolor("red")
l2.pencolor("blue")

def l1_move():
    l1.fd(50)

def l2_move():
    l2.penup()
    l2.setpos(10,10)
    l2.pendown()
    l2.fd(50)

t.ontimer(l1_move,1)
t.ontimer(l2_move,1)

t.mainloop()
