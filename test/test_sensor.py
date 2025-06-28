import unittest
from sensor import EntrySensor, ExitSensor
from car_park import CarPark

class TestSensorSubclasses(unittest.TestCase):

    def setUp(self):
        self.car_park = CarPark(location="Gate A", capacity=100)
        self.entry_sensor = EntrySensor(Sensor_Id=1, Is_active=True, Car_park=self.car_park)
        self.exit_sensor = ExitSensor(Sensor_Id=2, Is_active=True, Car_park=self.car_park)
    #Verifies that EntrySensor adds a new plate to the car park when detecting a vehicle.
    def test_entry_sensor_adds_car(self):
        initial_count = len(self.car_park.plates)
        self.entry_sensor.detect_vehicle()
        self.assertEqual(len(self.car_park.plates), initial_count + 1)
    #Verifies that ExitSensor removes an existing plate from the car park when detecting a vehicle.
    def test_exit_sensor_removes_car(self):
        test_plate = "TEST-001"
        self.car_park.add_car(test_plate)

        initial_count = len(self.car_park.plates)
        self.exit_sensor.detect_vehicle()
        self.assertLess(len(self.car_park.plates), initial_count)

