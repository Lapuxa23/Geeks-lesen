class Transport:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def change_color(self, new_color):
        print(f'Color changed to {new_color}')
        self.color = new_color


class Plane(Transport):
    def __init__(self, model, year, color):
        super().__init__(model, year, color)

    def fly(self):
        print(f'Plane {self.model} of color {self.color} is flying.')


class Car(Transport):
    # class attribute
    counter = 0

    # constructor          parameters
    def __init__(self, model, year, color, penalties=0):
        # attributes/fields
        super().__init__(model, year, color)
        self.penalties = penalties
        Car.counter += 1

    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')


class Truck(Car):
    counter = 0
    def __init__(self, model, year, color, penalties=0, load_capacity=0):
        super().__init__(model, year, color, penalties)
        self.load_capacity = load_capacity
        Truck.counter += 1

    def load_cargo(self, weight, type_of_cargo):
        if weight > self.load_capacity:
            print(f'You can not load more than {self.load_capacity} kg!')
        else:
            print(f'You successfully loaded cargo of {type_of_cargo} ({weight} kg.)')


print(f'Factory CAR produced: {Car.counter} cars.')
my_number = 7
print(my_number)
honda_car = Car('Honda Civic', 2019, 'red')
print(honda_car)
print(f'MODEL: {honda_car.model} YEAR: {honda_car.year} '
      f'COLOR: {honda_car.color} PENALTIES: {honda_car.penalties}')

bmw_car = Car('BMW X5', 2022, 'blue', 900)
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} '
      f'COLOR: {bmw_car.color} PENALTIES: {bmw_car.penalties}')
# bmw_car.color = 'black'
bmw_car.change_color('black')
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} '
      f'NEW COLOR: {bmw_car.color} PENALTIES: {bmw_car.penalties}')

toyota_car = Car(year=2000, model='Toyota Camry',
                 penalties=400, color='yellow')
print(f'MODEL: {toyota_car.model} YEAR: {toyota_car.year} '
      f'COLOR: {toyota_car.color} PENALTIES: {toyota_car.penalties}')
toyota_car.drive('Osh')
bmw_car.drive('Kant')

print(f'Factory CAR produced: {Car.counter} cars.')

boeing_plane = Plane('Boeing 747', 2024, 'white')
print(f'MODEL: {boeing_plane.model} YEAR: {boeing_plane.year} '
      f'COLOR: {boeing_plane.color}')
boeing_plane.fly()

volvo_truck = Truck('Volvo 300', 2021,
                    'orange', 1800, 35000)
print(f'MODEL: {volvo_truck.model} YEAR: {volvo_truck.year} '
      f'COLOR: {volvo_truck.color} PENALTIES: {volvo_truck.penalties} '
      f'LOAD CAPACITY: {volvo_truck.load_capacity} kg.')
volvo_truck.load_cargo(40000, 'tomatoes')
volvo_truck.load_cargo(10000, 'apples')
volvo_truck.drive('Tokmok')

print(f'Factory TRUCK produced: {Truck.counter} trucks.')

print('End of program')