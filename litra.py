import turtle as t  # import library
from time import sleep
screen=t.Screen()
print(screen)
screen._root.geometry("+200+200")
t.speed(10) # pen speed.
t.setup(width=1000, height=600) # declaring windows size
print(t.pos()) # pen position
t.penup()
t.setpos(-250,0)  # set pen position
t.pendown()
sleep(2)
def refractor(size):
    screen.title("Refractor telescope")
    t.pensize(size**2)
    t.pencolor("red")
    t.fd(50)
    t.color("black")
    t.write("l")
    t.pencolor("blue")
    t.fd(10)
    x=size**2
    for i in range(500):
        if x==1:
            break
        t.pencolor("red")
        t.pensize(x)
        t.fd(5)
        x-=1
        print(x)
    for i in range(20):
        x+=1
        t.pensize(x)
        t.fd(2)
    t.pencolor("black")
    t.fd(5)
    t.pencolor("red")
    t.fd(20)

refractor(10)
t.mainloop()