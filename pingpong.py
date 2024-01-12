import turtle
wind = turtle.Screen()
wind.title("Ping Pong.EXE")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

#racket1
racket1 = turtle.Turtle()
racket1.speed(0)
racket1.shape("square")
racket1.color("blue")
racket1.penup()
racket1.goto(-350, 0)
racket1.shapesize(stretch_len=1, stretch_wid=5)
#racket2
racket2 = turtle.Turtle()
racket2.speed(0)
racket2.shape("square")
racket2.color("red")
racket2.penup()
racket2.goto(350, 0)
racket2.shapesize(stretch_len=1, stretch_wid=5)
#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()     
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = -0.25

#scores
score1=0
score2=0
score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("player 1: 0 player 2: 0", align="center", font=("courier",24,"normal"))

#functions
def racket1_up():
    y=racket1.ycor()
    y+=20
    racket1.sety(y)

def racket1_down():
    y=racket1.ycor()
    y-=20
    racket1.sety(y)

def racket2_up():
    y=racket2.ycor()
    y+=20
    racket2.sety(y)

def racket2_down():
    y=racket2.ycor()
    y-=20
    racket2.sety(y)
#keyboard bindings
wind.listen()
wind.onkeypress(racket1_up, "w")
wind.onkeypress(racket1_down, "s")
wind.onkeypress(racket2_up, "Up")
wind.onkeypress(racket2_down, "Down")
while True:
    wind.update()
    #move ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #border check
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor()>390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 +=1
        score.clear()
        score.write("player 1: {} player 2: {}".format(score1, score2), align="center", font=("courier",24,"normal"))
    
    if ball.xcor()<-390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2+=1
        score.clear()
        score.write("player 1: {} player 2: {}".format(score1, score2), align="center", font=("courier",24,"normal"))

    
    #racket and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < racket2.ycor()+40 and ball.ycor()>racket2.ycor()-40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < racket1.ycor()+40 and ball.ycor()>racket1.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1



