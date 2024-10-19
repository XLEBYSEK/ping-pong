import turtle
import turtle as t
import os

win = t.Screen()
win.title("Ping-Pong Game")
win.bgcolor('black')
win.setup(width=800,height=600)
win.tracer(0)


paddle_left = t.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.color('red')
paddle_left.shapesize(stretch_wid=5,stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350,0)


paddle_right = t.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.shapesize(stretch_wid=5,stretch_len=1)
paddle_right.color('red')
paddle_right.penup()
paddle_right.goto(350,0)


ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('yellow')
ball.penup()
ball.goto(0,0)
ball_dx = 1.5
ball_dy = 1.5


pen = t.Turtle()
pen.speed(0)
pen.color('skyblue')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("PLayer A: 0                  Player B: 0", align="center",font=('Monaco',24,"normal"))


def paddle_left_up():
    
