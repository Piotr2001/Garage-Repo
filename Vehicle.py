def Function_select():
    V = int(input('''
    What function would you like to preform?
    =======================================
    1.List the vehicles
    2.Add a Vehicle
    3.Remove a Vehivle
    4.Replace a Vehicle
    5.Qutoe the fixing cost
    6.Exit
    ==============================================
    Please pick a number:
    '''))
    return V

def working():
    E = 0
    V = Function_select()
    while E != 6:
        if V == 1:
            List_Garage()
        elif V == 2:
            add_vehicle()
        elif V == 3:
            print ("3")
        elif V == 4:
            print ("4")
        elif V == 5:
            Quote_Vehicle()
        elif V == 6:
            print("You have decided to exit.")
            E = 6
        else:
            print ("Not a valid input")

def List_Garage():
    for vehicle in Garage:
            print(vars(vehicle))

def add_vehicle():
    print ("Adding")
    A = int(input('''
    What type of vehicle are you adding?
    1.Car
    2.Motorbike
    3.Van
    please pick a number:
    '''))
    reg = input('Please enter vehicle reg: ')
    colour = input('Please enter vehicle colour: ')
    condition = input('Please enter vehicle condition for A to D: ')
    if A == 1:
        type = int(input('''
        Please pick vehicle type:
        1.Hatch Back
        2.SUV
        3.Super Car
        4.Saloon
        5.Other
        Please pick a number: 
        '''))
        if type == 1:
            type = "Hatch Back"
        elif type == 2:
            type = "SUV"
        elif type == 3:
            type = "Super Car" 
        elif type == 4:
            type = "Saloon"
        elif type == 5:
            type = "Other"
        else:
            print("Not a valid input")
        no_doors = int(input("Please enter number of doors: "))
        Car = car(reg, colour, condition, type, no_doors)
        Garage.append(Car)
        for vehicle in Garage:
            print(vars(vehicle))
    elif A == 2:
        type = input("Please enter vehicle type: ")
        Bike = motorbike(reg, colour, condition, type)
    elif A == 3:
        type = input("Please enter vehicle type: ")
        size = input("Please enter vehicle size: ")
        Van = van(reg, colour, condition, type, size)
    else:
        print("Not a valid input")

def Quote_Vehicle():
    cost = 100
    
    if condition == "A":
        cost = cost * 1.2
    elif condition == "B":
        cost = cost * 1.5
    
class Vehicle:
    def __init__(self, reg, colour, condition):
        self.reg = reg
        self.colour = colour
        self.condition = condition

class motorbike(Vehicle):
    def __init__(self, reg, colour, condition, type):
        super().__init__(reg, colour, condition)
        self.type = type

class van(Vehicle):
    def __init__(self, reg, colour, condition, type, size):
        super().__init__(reg, colour, condition)
        self.type = type
        self.size = size

class car(Vehicle):
    def __init__(self, reg, colour, condition, type, no_doors):
        super().__init__(reg, colour, condition)
        self.type = type
        self.no_doors = no_doors

First_car = car("abx342", "Red", "D", "SUV", 5)
Garage = [First_car] 
working()