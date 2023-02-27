# Objectives
# improving the student's skills in operating with inheritance and composition
# Scenario
# Imagine that you are an automotive fan, and you are able to build a car
# from a limited set of components.
#
# Your task is to :
#
# define classes representing:

# tires (as a bundle needed by a car to operate);
# methods available: get_pressure(), pump();
# attribute available: size

# engine;
# methods available: start(), stop(), get_state();
# attribute available: fuel type

# vehicle;
# method available: __init__(VIN, engine, tires);
# attribute available: VIN

# based on the classes defined above, create the following objects:
#   two sets of tires: city tires (size: 15), off-road tires
#   (size: 18)
#   two engines: electric engine, petrol engine
# instantiate two objects representing cars:
#   the first one is a city car, built of an electric engine and
#   city tires
#   the second one is an all-terrain car build of a petrol engine
#   and
#   off-road tires
# play with the cars by calling methods responsible for interaction
# with components.

class Tyres:
    def __init__(self, size):
        self.size = size

    def get_pressure(self):
        return f"Reading tyre pressure... {self.size}"

    def pump(self):
        return "Pumping tyres... "


class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start(self):
        return "Starting {} engine".format(self.engine_type)

    def stop(self):
        return "Stopping {} engine".format(self.engine_type)

    def get_state(self):
        return "Type of engine in this car: {}".format(self.engine_type)


class Vehicle:
    def __init__(self, vin, engine, tyres):
        # vehicle identification number (VIN)
        self.vin = vin
        self.engine = engine
        self.tyres = tyres


city_tyres = Tyres(15)
off_road_tyres = Tyres(18)

electric_engine = Engine("Electric")
petrol_engine = Engine("Petrol")

city_car = Vehicle("66000", electric_engine, city_tyres)
all_terrain_car = Vehicle("88000", petrol_engine, off_road_tyres)

print(city_car.engine.start())
print(city_car.engine.get_state())
print(city_car.engine.stop())
print(city_car.engine.get_state())

print(all_terrain_car.tyres.pump())
print(all_terrain_car.tyres.get_pressure())

# near enough!
