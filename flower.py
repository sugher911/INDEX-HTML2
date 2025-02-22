# import qrcode 

# qr_img = qrcode.make("you are hacked!👿\n your phone \n to blackhate hacker:")

# qr_img.save("qr-img.jpg")

# t = 99 
# v = 22 
# hello = t/v
# print(hello +


import turtle  

def draw_petal(color):
    turtle.color(color)
    for _ in range(2):  
        turtle.circle(100, 60)  
        turtle.left(120)  
        turtle.circle(100, 60)  
        turtle.left(120)  

def draw_flower(num_petals):
    turtle.speed(0)
    colors = ["red", "blue", "purple", "pink", "orange", "yellow"]

    for i in range(num_petals):  
        draw_petal(colors[i % len(colors)])  
        turtle.right(360 / num_petals)  

    # Draw flower center
    turtle.color("yellow")  
    turtle.dot(80)  
    turtle.hideturtle()  

# Set up turtle screen
turtle.bgcolor("black")  
turtle.penup()  
turtle.goto(0, -50)  
turtle.pendown()  
draw_flower(12)  # Change number of petals here

turtle.done()
