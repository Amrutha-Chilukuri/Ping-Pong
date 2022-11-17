from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
game_is_on = True

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

scoreboard = Scoreboard()
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()

    elif ball.xcor()>380:
        scoreboard.r_point()
        ball.reset_position()

    elif ball.xcor()<-380:
        scoreboard.l_point()
        ball.reset_position()

screen.exitonclick()
