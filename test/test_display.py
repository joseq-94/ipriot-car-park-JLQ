import unittest
from display import Display
from car_park import CarPark

class TestDisplay(unittest.TestCase):

    def setUp(self):
        self.car_park = CarPark(location="Entrance", capacity=100)
        self.display = Display(
            display_Id=1,
            Message="Welcome to the car park",
            Is_on=True,
            car_park=self.car_park
        )

    def test_display_initialized_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.display_Id, 1)
        self.assertEqual(self.display.Message, "Welcome to the car park")
        self.assertEqual(self.display.Is_on, True)

    def test_update(self):
        self.display.update({"Message": "Goodbye"})
        self.assertEqual(self.display.Message, "Goodbye")
