from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20

NORTH = 90
SOUTH = 270
WEST = 180
EAST = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle_sq = Turtle(shape="square")
        new_turtle_sq.penup()
        new_turtle_sq.color("white")
        new_turtle_sq.goto(position)
        self.segments.append(new_turtle_sq)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVING_DISTANCE)

    def north(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def south(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)

    def east(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

    def west(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)
