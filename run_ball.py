import turtle
from ball import Ball

turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
turtle.colormode(255)
ball = Ball()
ball.initilizing()
while (True):
    turtle.clear()
    for i in range(ball.num_balls):
        ball.draw_circle(i)
        ball.move_circle(i)
    turtle.update()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
