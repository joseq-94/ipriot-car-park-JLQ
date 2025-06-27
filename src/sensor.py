class Sensor:
    def __init__(self, Sensor_Id, Is_active, Car_park):
        self.Sensor_Id = Sensor_Id
        self.Is_active = Is_active
        self.Car_park = Car_park

    def __str__(self):
        status = "Active" if self.Is_active else "Inactive"
        return f"Sensor {self.Sensor_Id} is {status}"

class EntrySensor(Sensor):
    def __init__(self, Sensor_Id, Is_active, Car_park):
        super().__init__(Sensor_Id, Is_active, Car_park)

class ExitSensor(Sensor):
    def __init__(self, Sensor_Id, Is_active, Car_park):
        super().__init__(Sensor_Id, Is_active, Car_park)