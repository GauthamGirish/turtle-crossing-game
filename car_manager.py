from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self, level):
        super().__init__()
        self.shape("square")
        self.shapesize(1,2)
        self.color(random.choice(COLORS))
        self.penup()
        self.left(180)
        self.teleport(300, random.randint(-250,250))
        self.car_speed=STARTING_MOVE_DISTANCE+(level-1)*MOVE_INCREMENT

    def move(self):
        self.forward(self.car_speed)

    @staticmethod
    def move_all_cars(cars: list):
        for car in cars.copy():
            car.move()
            if car.xcor()<-320:
                cars.remove(car)

    @staticmethod
    def clear_all_cars(cars: list):
        for car in cars:
            car.hideturtle()
        cars.clear()
