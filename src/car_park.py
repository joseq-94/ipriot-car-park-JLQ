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
        return f"Welcome to {self.location} CarPark | Capacity: {self.capacity}"

    #this method will allow the car park to register sensors and display
    def register(self, component):
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)
        else:
            raise TypeError("Object must be a sensor or display")

    def add_car(self, plate):
        self.plates.append(plate)

    def remove_car(self,plate):
        self.plates.remove(plate)

    def Update_displays(self):
        for display in self.displays:
            display.update(self.available_bays)
            print(f"Car {display} updated.")


    @property
    def available_bays(self):
        #car_park.available_bays
        return max(0, self.capacity - len(self.plates))
