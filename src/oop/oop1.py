# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


# BELOW WILL BE THE BASE CLASS 'VEHICLE'
class Vehicle:
    pass
    # def __init__(self, name):
    #     self.name = name


class GroundVehicle(Vehicle):
    pass
    # def __init__(self, name):
    # self.num_wheels = num_wheels
    # self.drive = drive
    # super.__init__(self, name)

    # def drive(self):
    #     return "vroooom"


class Motorcycle(GroundVehicle):
    pass
    # def __init__(self, name):
    #     super.__init__(self, name)


class Car(GroundVehicle):
    pass
    # def __init__(self, name):
    #     super.__init__(self, name)


class FlightVehicle(Vehicle):
    pass
    # def __init__(self, name):
    #     super.__init__(self, name)


class Airplane(FlightVehicle):
    pass
    # def __init__(self, name):
    #     super.__init__(self, name)


class Starship(FlightVehicle):
    pass
    # def __init__(self, name):
    #     super.__init__(self, name)
