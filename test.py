import turtle as t 
t.speed(10)
x=50
t.pensize(x)
t.pencolor("blue")
t.fd(10)
t.pencolor("red")
for i in range(500):
    if(x==1):
        break
    t.pensize(x)
    t.forward(5)
    x-=1
t.write("p")
t.mainloop()
