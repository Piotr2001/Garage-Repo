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
    V = Function_select()
    if V == 1:
        List_Garage()
    elif V == 2:
        print ("2")
    elif V == 3:
        print ("3")
    elif V == 4:
        print ("4")
    elif V == 5:
        print ("5")
    elif V == 6:
        print ("6")
    else:
        print ("Not a valid input")

working()

def List_Garage():
    print (Garage)

def Add_Vehicle():
    print ("Adding")
    
class Vehicle:
    def __init__(self, reg, colour):
        self.reg = reg
        self.colour = colour

class Motorbike(Vehicle):
    def __init__(self, reg, colour, type, condition):
        super().__init__(reg, colour)
        self.type = type
        self.condition = condition

class Van(Vehicle):
    def __init__(self, reg, colour, type, condition, size):
        super().__init__(reg, colour)
        self.type = type
        self.condition = condition
        self.size = size

class car(Vehicle):
    def __init__(self, reg, colour, type, condition, no_doors):
        super().__init__(reg, colour)
        self.type = type
        self.condition = condition
        self.no_doors = no_doors
