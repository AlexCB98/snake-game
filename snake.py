import turtle as t

POSITION = [(0,0), (-20,0), (-40,0)]
MOVE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for each_position in POSITION:
            square = t.Turtle('square')
            square.color('gray')
            square.penup()
            square.goto(each_position)
            self.segments.append(square)

    def move(self):
        for seg_n in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_n - 1].xcor()
            new_y = self.segments[seg_n - 1].ycor()
            self.segments[seg_n].goto(new_x, new_y)
        self.segments[0].forward(MOVE)

