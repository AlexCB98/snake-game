import turtle as t

screen = t.Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('My Snake Game')

position = [(0,0), (-20,0), (-40,0)]

for each_position in position:
    square = t.Turtle('square')
    square.color('gray')
    square.goto(each_position)







screen.exitonclick()