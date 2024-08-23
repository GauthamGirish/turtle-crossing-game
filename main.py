import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
score=Scoreboard()
cars=[]

screen.listen()
screen.onkeypress(player.move, "Up")

nc=0
time_to_next_car=0
game_is_on = True
while game_is_on:
    if nc>=time_to_next_car:
        nc=0
        time_to_next_car=random.randint(5,10)
        cars.append(CarManager(score.level))
    CarManager.move_all_cars(cars)
    if player.check_collision(cars):
        score.game_over()
        screen.update()
        break
    if player.cross_finish():
        score.increase_level()
        CarManager.clear_all_cars(cars)
        player.teleport(0,-280)
    nc=nc+1
    time.sleep(0.1)
    screen.update()
screen.exitonclick()
