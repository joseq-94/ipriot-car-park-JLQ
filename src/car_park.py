from sensor import Sensor
from display import Display


class CarPark:
    def __init__(self, location = "Unknown", capacity = 100, plates = None, display = None,
                 sensors = None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = display or []
        self.sensors = sensors or []

    def __str__(self):
        return f"CarPark en {self.location} | Capacity: {self.capacity}"

    #this method will allow the car park to register sensors and display
    def register(self, component):
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)
        else:
            raise TypeError("Object must be a sensor or display")

    def add_car(self, plate):
        if len(self.plates) < self.capacity:
            self.plates.append(plate)
            print(f"Car {plate} entered.")
        else:
            print("Car park full. Cannot add more vehicles.")
        self.Update_displays()

    def remove_car(self,plate):
        if plate in self.plates:
            self.plates.remove(plate)
            print(f"Car {plate} exited.")
        else:
            print(f"Car {plate} not found.")
        self.Update_displays()

    def Update_displays(self):
        for display in self.displays:
            display.update(self)

    def available_bays(self):
        return self.capacity - len(self.plates)
    if available_bays() == 0:
        print("No available bays.")



