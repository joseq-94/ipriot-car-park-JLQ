import random
from abc import ABC, abstractmethod

class Sensor(ABC):
    def __init__(self, Sensor_Id, Is_active, Car_park):
        self.Sensor_Id = Sensor_Id
        self.Is_active = Is_active
        self.Car_park = Car_park

    def __str__(self):
        status = "Active" if self.Is_active else "Inactive"
        return f"Sensor {self.Sensor_Id} is {status}"

    @abstractmethod
    def update_car_park(self, plate):
        pass

    def _scan_plate(self):
        return 'Fake-' + format(random.randint(0, 999), "03d")

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)

class EntrySensor(Sensor):
    def __init__(self, Sensor_Id, Is_active, Car_park):
        super().__init__(Sensor_Id, Is_active, Car_park)

    def update_car_park(self, plate):
        self.Car_park.add_car(plate)
        print(f"incoming vehicle detect. Plate:  {plate}")

class ExitSensor(Sensor):
    def __init__(self, Sensor_Id, Is_active, Car_park):
        super().__init__(Sensor_Id, Is_active, Car_park)

    def update_car_park(self, plate):
        self.Car_park.remove_car(plate)
        print(f"outcoming vehicle detect. Plate:  {plate}")

    def _scan_plate(self):
        return random.choice(self.Car_park.plates)

