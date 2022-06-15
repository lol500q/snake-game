from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
FONT=('Arial',15,'italic')


class Snake:

    def __init__(self):
        self.segments = []
        self.turtle12=Turtle()
        self.turtle12.hideturtle()
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading()==DOWN:
            return
        else:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()==UP:
            return
        else:

            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()==RIGHT:
            return
        else:


            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()==LEFT:
            return
        else:



            self.head.setheading(RIGHT)
    def is_hit_wall(self):

        if self.head.xcor() < -280 or self.head.xcor() > 290 or self.head.ycor()<-290 or self.head.ycor()>290:


            self.turtle12.color('white')
            self.turtle12.penup()
            self.turtle12.hideturtle()
            self.turtle12.goto(0,0)
            self.turtle12.write("Game Over:")
            return False
        else:
            return True



    def pause(self):
        return False
    def increase_snake(self):
        increase_turtle=Turtle()
        increase_turtle.hideturtle()
        increase_turtle.penup()
        increase_turtle.setposition(-60,0)
        increase_turtle.showturtle()
        increase_turtle.color('white')
        increase_turtle.shape('square')
        self.segments.append(increase_turtle)
    def is_hit_his_tail(self):
        for i in self.segments[1:]:
            if self.head.distance(i) < 15:
                self.turtle12.color('white')
                self.turtle12.penup()
                self.turtle12.hideturtle()
                self.turtle12.goto(0, 0)
                self.turtle12.write("Game Over:")
                return False

        return True











#