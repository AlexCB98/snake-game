import turtle as t

from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = t.Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

restart_button = t.Turtle()
restart_button.color('white')
restart_button.penup()
restart_button.hideturtle()
restart_button.goto(0, 0)


def restart_game(x, y):
    global game_is_on

    if not game_is_on and -60 < x < 60 and -20 < y < 20:
        restart_button.clear()
        snake.reset()
        food.refresh()
        game_is_on = True


screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onclick(restart_game)



game_is_on = True

while True:
    screen.update()
    time.sleep(0.05)

    if game_is_on:
        snake.move()

        # Collision with food and extend.

        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Collision with wall.

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.reset()
            game_is_on = False
            restart_button.write('Restart', align='center', font=('Courier', 20, 'normal'))

        # Collision with tail.

        if game_is_on:
            for segment in snake.segments[2:]:
                if snake.head.distance(segment) < 8:
                    scoreboard.reset()
                    game_is_on = False
                    restart_button.write('Restart', align='center', font=('Courier', 20, 'normal'))





screen.update()
screen.exitonclick()
