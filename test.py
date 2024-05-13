import turtle as t

# Set up the screen
screen = t.Screen()
screen.setup(width=800, height=600)
screen.title("Reflective Telescope Simulation")
t.speed(1)
# t.pensize(50)
# Draw the optical setup
def draw_optical_setup():
    # Draw the mirror
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    t.setheading(90)
    t.forward(100)
    t.left(90)
    t.forward(400)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(400)
    
    # Draw the light source
    t.penup()
    t.goto(-250, 150)
    t.dot(10, "yellow")
    
    # Draw the light rays
    t.penup()
    t.goto(-250, 150)
    t.pendown()
    t.setheading(70)
    t.forward(300)
    
    t.penup()
    t.goto(-250, 150)
    t.pendown()
    t.setheading(110)
    t.forward(300)

# Main function to run the simulation
def main():
    t.speed(0)
    draw_optical_setup()
    t.hideturtle()
    t.done()

if __name__ == "__main__":
    main()
