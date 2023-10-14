
total_car = 5


class Car:
    size = 30

    def __init__(self, windows: int):
        self.wheels = 4
        self.windows = windows
        print("Initializing the blueprint of a Car")

    def description(self, color):
        color_type = "Light"
        print(f'The color of the car is "{color_type} {color}" and has {self.windows} windows. The '
              f'size is {self.size}ft')

    def print_total_car(self):
        # global total_car
        print(f'Total number of car is: {total_car}')


ferrari = Car(6)
ferrari.description("Red")
ferrari.print_total_car()
