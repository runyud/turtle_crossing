from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.speed = 1

    def generate_cars(self):
        # generate initial set of cars
        car = Turtle()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        random_y = random.randint(-200, 250)
        car.goto(250, random_y)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT * self.speed)

    def increase_speed(self):
        self.speed += 0.5
