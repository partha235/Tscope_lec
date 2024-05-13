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

def reflector():
    # light entering 
    t.speed(1) # pen speed.
    t.setup(width=1000, height=600) # declaring windows size
    print(t.pos()) # pen position
    t.pencolor("red")
    t.penup()
    t.setpos(-250,0) 
    sleep(2)

    # light entering
    t.pendown()
    t.pensize(100)
    t.fd(50)
    t.penup()
    t.fd(5+5+10+30+2)
    t.pencolor("black")
    t.pendown()
    t.pensize(20)
    t.fd(5)



    # light ray in side of secondary mirror
    l1=t.Turtle()
    l2=t.Turtle()
    l1.penup()
    l2.penup()
    l1.setpos(-158,30)
    l2.setpos(-158,-30)
    l1.pendown()
    l2.pendown()
    l1.setheading(0)
    l2.setheading(0)
    l1.bk(30)
    l2.bk(30)
    l1.pensize(35)
    l1.pencolor("red")
    l2.pensize(35)
    l2.pencolor("red")
    l1.fd(230)
    l2.fd(230)

    # drawing reflective mirror
    t.penup()
    t.bk(5)
    t.fd(200)
    t.pendown()
    t.fillcolor("blue")
    t.begin_fill()
    t.pensize(1)
    t.setheading(270)
    t.fd(50)
    t.left(90)
    t.fd(10)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(10)
    t.left(90)
    t.fd(50)
    t.end_fill()


    # reflecting light
    l1.pencolor("blue")
    l1.pensize(5)
    l1.right(170)
    l1.fd(178)
    l1.setheading(270)
    l1.fd(100)


    l2.pencolor("blue")
    l2.pensize(5)
    l2.left(170)
    l2.fd(178)
    l2.setheading(270)
    l2.fd(100) 

# reflector()
t.mainloop()