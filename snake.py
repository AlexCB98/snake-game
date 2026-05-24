import turtle as t

POSITION = [(0,0), (-20,0), (-40,0)]

MOVE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color('orange')

    def create_snake(self):
        for each_position in POSITION:
            self.add_segment(each_position)


    def add_segment(self, each_position):
        segment = t.Turtle('circle')
        segment.color('blue')
        segment.penup()
        segment.goto(each_position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_n in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_n - 1].xcor()
            new_y = self.segments[seg_n - 1].ycor()
            self.segments[seg_n].goto(new_x, new_y)
        self.segments[0].forward(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


