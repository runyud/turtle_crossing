import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carManager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
loop_times = 0
while game_is_on:
    if loop_times % 6 == 0:
        # generate cars
        carManager.generate_cars()

    carManager.move_cars()

    # detect when the turtle player collides with the car
    for car in carManager.cars:
        if car.distance(player) < 30:
            score_board.game_over()
            game_is_on = False

    # detect when the turtle player reached the top edge
    if player.ycor() == 250:
        score_board.increase_score()
        player.goto(0, -250)
        carManager.increase_speed()

    time.sleep(0.2)
    screen.update()
    loop_times += 1

screen.exitonclick()
