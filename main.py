import turtle as t
import time

screen = t.Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

position = [(0,0), (-20,0), (-40,0)]
segments = []

for each_position in position:
    square = t.Turtle('square')
    square.color('gray')
    square.penup()
    square.goto(each_position)
    segments.append(square)



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_n in range(len(segments) -1, 0, -1):
        new_x = segments[seg_n -1].xcor()
        new_y = segments[seg_n -1].ycor()
        segments[seg_n].goto(new_x, new_y)
    segments[0].forward(20)




screen.update()
screen.exitonclick()