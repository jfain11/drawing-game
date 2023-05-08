import turtle

wn = turtle.Screen()
wn.bgcolor("white")
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 360)
pen.write("[1] BLACK | [2] BLUE | [3] RED | [4] YELLOW | [5] ERASER", align="center", font=("Courier", 20, "bold"))

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("black")
pen2.penup()
pen2.hideturtle()
pen2.goto(0, -380)
pen2.write(" [UP-ARROW] UP  | [LEFT-ARROW] LEFT | [DOWN-ARROW] DOWN | [RIGHT-ARROW] RIGHT |  [R] RESET ", align="center", font=("Courier", 12, "bold"))

player = turtle.Turtle()
player.speed(0)
player.goto(0, 0)
player.shape("circle")
player.color("white")
player.shapesize(.5, .5, .5)
player.pencolor("black")
player.pensize(15)

line1 = turtle.Turtle()
line1.speed(1)
line1.penup()
line1.goto(480, -335)
line1.pendown()
line1.shape("circle")
line1.color("black")
line1.shapesize(.1, .1, .1)
line1.pencolor("black")
line1.pensize(7)
line1.right(180)
line1.forward(1000)

line2 = turtle.Turtle()
line2.speed(0)
line2.penup()
line2.goto(480, 345)
line2.pendown()
line2.shape("circle")
line2.color("black")
line2.shapesize(.1, .1, .1)
line2.pencolor("black")
line2.pensize(7)
line2.right(180)
line2.forward(1000)

line3 = turtle.Turtle()
line3.speed(0)
line3.penup()
line3.goto(110, -335)
line3.pendown()
line3.shape("circle")
line3.color("black")
line3.shapesize(.1, .1, .1)
line3.pencolor("black")
line3.pensize(7)
line3.right(90)
line3.forward(100)
line3.penup()
line3.goto(330, -335)
line3.pendown()
line3.forward(100)
line3.penup()
line3.goto(468, -335)
line3.pendown()
line3.forward(100)
line3.penup()
line3.goto(-90, -335)
line3.pendown()
line3.forward(100)
line3.penup()
line3.goto(-290, -335)
line3.pendown()
line3.forward(100)
line3.penup()
line3.goto(-475, -335)
line3.pendown()
line3.forward(100)





def clear():
    player.clear()

def up():
    y = player.ycor()
    y += 50
    player.sety(y)


def down():
    y = player.ycor()
    y -= 50
    player.sety(y)


def left():
    x = player.xcor()
    x -= 50
    player.setx(x)


def right():
    x = player.xcor()
    x += 50
    player.setx(x)


def erase():
    player.pencolor("white")


def drawblack():
    player.pencolor("black")


def drawred():
    player.pencolor("red")


def drawblue():
    player.pencolor("blue")


def drawyellow():
    player.pencolor("yellow")


wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(erase, "5")
wn.onkeypress(drawblack, "1")
wn.onkeypress(drawblue, "2")
wn.onkeypress(drawred, "3")
wn.onkeypress(drawyellow, "4")
wn.onkeypress(clear, "r")


while True:
    wn.update()
