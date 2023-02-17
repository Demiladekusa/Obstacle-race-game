import turtle
import math

#turtle screen

s = turtle.Screen()
s.title("Turtle obstacle mission")
s.bgpic("picss.gif")

# creating a boarder
boarder = turtle.Turtle()
boarder.penup()
boarder.setpos(-675,-340)
boarder.pensize(3)
boarder.pendown()
boarder.speed(20)
for i in range(2):
    boarder.forward(1343)
    boarder.left(90)
    boarder.forward(683)
    boarder.left(90)
boarder.hideturtle()

# game instruction
print("GET TO THE GREEN LINE TO COMPLETE THE MISSION")
print("avoid the red obsatcles")
GameOver = "MISSION COMPLETE"

# creating a finish line
line = turtle.Turtle()
line.penup()
line.speed(20)
line.color('green')
line.setpos(630,-340)
line.pensize(3)
line.rt(270)
line.pendown()
line.fd(680)
line.speed(20)
line.hideturtle()

# creating player one
Player = turtle.Turtle()
Player.penup()
Player.shapesize(2)
Player.color('blue')
Player.shape('classic')
Player.setpos(-660,0)


# creating obstacle 1
obstacle = turtle.Turtle()
obstacle.color('red')
obstacle.shape('square')
obstacle.shapesize(4)
obstacle.penup()
obstacle.right(270)
obstacle.setpos(-530,10)

# creating obstacle 2
obstacle2 = turtle.Turtle()
obstacle2.color('red')
obstacle2.shape('square')
obstacle2.shapesize(3)
obstacle2.penup()
obstacle2.right(270)
obstacle2.setpos(-200,-100)

# creating obstacle 3
obstacle3 = turtle.Turtle()
obstacle3.color('red')
obstacle3.shape('square')
obstacle3.shapesize(3)
obstacle3.penup()
obstacle3.right(270)
obstacle3.setpos(150,0)

# creating obstacle 4
obstacle4 = turtle.Turtle()
obstacle4.color('red')
obstacle4.shape('square')
obstacle4.shapesize(3)
obstacle4.penup()
obstacle4.right(270)
obstacle4.setpos(460,20)


# creating obstacle 5
obstacle5 = turtle.Turtle()
obstacle5.color('red')
obstacle5.shape('square')
obstacle5.shapesize(1)
obstacle5.penup()
obstacle5.right(270)
obstacle5.setpos(580,-15)


# creating obstacle 6
obstacle6 = turtle.Turtle()
obstacle6.color('red')
obstacle6.shape('square')
obstacle6.shapesize(3)
obstacle6.penup()
obstacle6.setpos(100,250)


# creating obstacle 7
obstacle7 = turtle.Turtle()
obstacle7.color('red')
obstacle7.shape('square')
obstacle7.shapesize(3)
obstacle7.penup()
obstacle7.setpos(-70,50)


# creating obstacle 8
obstacle8 = turtle.Turtle()
obstacle8.color('red')
obstacle8.shape('square')
obstacle8.shapesize(3)
obstacle8.penup()
obstacle8.setpos(-30,-100)


# creating obstacle 9
obstacle9 = turtle.Turtle()
obstacle9.color('red')
obstacle9.shape('square')
obstacle9.shapesize(3)
obstacle9.penup()
obstacle9.setpos(0,-260)


# creating speed variable
speed = 1

# creating functions
def up():
   Player.setheading(90)
   Player.forward(20)

def down():
    Player.setheading(270)
    Player.forward(20)

def left():
    Player.setheading(180)
    Player.forward(20)

def right():
   Player.setheading(0)
   Player.forward(20)


# onkey functions
turtle.listen()
turtle.onkey(right, 'Right')
turtle.onkey(up, 'Up')
turtle.onkey(left, 'Left')
turtle.onkey(down, 'Down')

while True:
    Player.forward(speed)

    #checking for collision of boader by player
    if Player.xcor() > 675 or  Player.xcor() < -675:
        Player.right(180)
    if Player.ycor() > 340 or Player.ycor() < -340:
         Player.right(180)

    # obstacle 1
    a = math.sqrt(math.pow(Player.xcor() - obstacle.xcor(), 2) + math.pow(Player.ycor() - obstacle.ycor(), 2))
    if a < 70:
        Player.setpos(-660,0)
        obstacle.setpos(-530,10)


    # moving obstacle 1
    obstacle.forward(150)

    #checking boader obstacle 1
    if obstacle.xcor() > 590 or  obstacle.xcor() < -610:
       obstacle.right(180)
    if obstacle.ycor() > 200 or obstacle.ycor() < -200:
        obstacle.right(180)

        #obstacle 2
    b = math.sqrt(math.pow(Player.xcor() - obstacle2.xcor(), 2) + math.pow(Player.ycor() - obstacle2.ycor(), 2))
    if b < 70:
        Player.setpos(-660, 0)
        obstacle2.setpos(-200,-260)


     #  obstacle 2 speed
    obstacle2.forward(140)

    # checking boader for obstacle 2
    if obstacle2.xcor() > 661 or obstacle2.xcor() < -665:
        obstacle2.right(180)
    if obstacle2.ycor() > 220 or obstacle2.ycor() < -200:
        obstacle2.right(180)

        # obstacle 3
    c = math.sqrt(math.pow(Player.xcor() - obstacle3.xcor(), 2) + math.pow(Player.ycor() - obstacle3.ycor(), 2))
    if c < 70:
        Player.setpos(-660, 0)
        obstacle3.setpos(150,0)

        # moving obstacle 3
    obstacle3.forward(200)

    # checking boader for obstacle 3
    if obstacle3.xcor() > 661 or obstacle3.xcor() < -665:
        obstacle3.right(180)
    if obstacle3.ycor() > 180 or obstacle3.ycor() < -200:
        obstacle3.right(180)

     # obstacle 4
    d = math.sqrt(math.pow(Player.xcor() - obstacle4.xcor(), 2) + math.pow(Player.ycor() - obstacle4.ycor(), 2))
    if d < 70:
        Player.setpos(-660, 0)
        obstacle4.setpos(460,20)


     # moving obstacle 4
    obstacle4.forward(120)

    # checking boader for obstacle 4
    if obstacle4.xcor() > 661 or obstacle4.xcor() < -665:
        obstacle4.right(180)
    if obstacle4.ycor() > 100 or obstacle4.ycor() < -150:
        obstacle4.right(180)

        # obstacle 5
    e = math.sqrt(math.pow(Player.xcor() - obstacle5.xcor(), 2) + math.pow(Player.ycor() - obstacle5.ycor(), 2))
    if e < 40:
        Player.setpos(-660, 0)
        obstacle5.setpos(580,-15)

        # moving obstacle 5
    obstacle5.forward(150)
        # checking boader obstacle 5
    if obstacle5.xcor() > 610 or obstacle5.xcor() < -610:
        obstacle5.right(180)
    if obstacle5.ycor() > 150 or obstacle5.ycor() < -120:
        obstacle5.right(180)

     # obstacle 6
    f = math.sqrt(math.pow(Player.xcor() - obstacle6.xcor(), 2) + math.pow(Player.ycor() - obstacle6.ycor(), 2))
    if f < 50:
        Player.setpos(-660, 0)
        obstacle6.setpos(100,250)


        # moving obstacle 6
    obstacle6.forward(150)
        # checking boarder obstacle 6
    if obstacle6.xcor() > 410 or obstacle6.xcor() < -350:
        obstacle6.right(180)
    if obstacle6.ycor() > 300 or obstacle6.ycor() < -330:
        obstacle6.right(180)

        # obstacle 7
    g = math.sqrt(math.pow(Player.xcor() - obstacle7.xcor(), 2) + math.pow(Player.ycor() - obstacle7.ycor(), 2))
    if g < 50:
        Player.setpos(-660, 0)
        obstacle7.setpos(-300,50)

        # moving obstacle 7
    obstacle7.forward(150)
    # checking boarder obstacle 7
    if obstacle7.xcor() > 410 or obstacle7.xcor() < -110:
        obstacle7.right(180)
    if obstacle7.ycor() > 300 or obstacle7.ycor() < -330:
        obstacle7.right(180)

    # obstacle 8
    h = math.sqrt(math.pow(Player.xcor() - obstacle8.xcor(), 2) + math.pow(Player.ycor() - obstacle8.ycor(), 2))
    if h < 50:
        Player.setpos(-660, 0)
        obstacle8.setpos(-30,-100)

        # moving obstacle 8
    obstacle8.forward(150)
    # checking boarder obstacle 8
    if obstacle8.xcor() > 250 or obstacle8.xcor() < -50:
        obstacle8.right(180)
    if obstacle8.ycor() > 300 or obstacle8.ycor() < -330:
        obstacle8.right(180)

        # obstacle 9
    j = math.sqrt(math.pow(Player.xcor() - obstacle9.xcor(), 2) + math.pow(Player.ycor() - obstacle9.ycor(), 2))
    if j < 50:
        Player.setpos(-660, 0)
        obstacle9.setpos(0,-260)

     # moving obstacle 9
    obstacle9.forward(150)
    # checking boarder obstacle 9
    if obstacle9.xcor() > 5 or obstacle9.xcor() < -350:
        obstacle9.right(180)
    if obstacle9.ycor() > 300 or obstacle9.ycor() < -330:
        obstacle9.right(180)

    # checking for finish line
    if Player.xcor() > 630:
       boarder.penup()
       boarder.hideturtle()
       boarder.setpos(0,0)
       GameOverstring = "%s " %GameOver
       boarder.write(GameOverstring, False, font=("airal",40,"normal"))
       break


turtle.done()

