import turtle as t  # import library
from time import sleep

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
l1.penup()
l1.fd(15)
l2.penup()
l2.fd(15)
l1.pendown()
l2.pendown()

# drawing reflective mirror
t.penup()
t.bk(5)
t.fd(180)
t.fillcolor("blue")
t.begin_fill()
t.pensize(1)
t.setpos(53,-5) 
t.pendown()
t.setheading(0)
t.fd(10)
t.setheading(270)
t.fd(50)
t.setheading(180)
t.fd(15)
t.setheading(72)
t.circle(125,23)
t.penup()
t.end_fill()
t.setpos(53,5)
t.pendown()
t.begin_fill()
t.setheading(90)
t.circle(200,15)
t.setheading(0)
t.fd(15)
t.setheading(270)
t.fd(51)
t.setheading(180)
t.fd(9)
t.hideturtle()
t.end_fill()

# reflecting light
l1.pencolor("blue")
l1.pensize(5)
l1.setheading(188)
l1.fd(190)
l1.setheading(359)
l1.fd(210)
l2.pencolor("green")
l2.pensize(5)
l2.setheading(173)
l2.fd(190)
l2.setheading(2)
l2.fd(210)

t.mainloop()