from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.new_level()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def new_level(self):
        self.teleport(*STARTING_POSITION)

    def check_collision(self, cars):
        for car in cars:
            carx,cary=car.pos()
            if carx<35 and carx>-35:
                if abs(cary-self.ycor())<=20:
                    return True
        return False

    def cross_finish(self):
        if self.ycor()>300:
            return True
        return False
