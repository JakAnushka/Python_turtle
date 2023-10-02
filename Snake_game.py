from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen= Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Right",fun=snake.right)
screen.onkey(key="Left",fun=snake.left)

game_is_on= True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    #distance function of turtle is used
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extention_snake()
        scoreboard.increase_score()

    # collision wall.
    if snake.head.xcor()>280 or snake.head.xcor()< -280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.reset_scoreboard()

        snake.reset_game()

    #collision with tail
    for segment in snake.segments[1:]:

        if segment==snake.head:
            pass
        if snake.head.distance(segment)<10:
            scoreboard.reset_scoreboard()

            snake.reset_game()





screen.exitonclick()