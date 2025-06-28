import random
import json
from pathlib import Path
from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display


# TODO: create a car park object with the location moondalup, capacity 100, and log_file "moondalup.txt"
Car_park = CarPark(location= "moondalup", capacity=100, log_file=Path("moondalup.txt"))

# TODO: Write the car park configuration to a file called "moondalup_config.json"
config_file = Path("moondalup_config.json")
with config_file.open("w") as f:
    json.dump({
        "location": Car_park.location,
        "capacity": Car_park.capacity,
        "log_file": str(Car_park.log_file)}, f)

# TODO: Reinitialize the car park object from the "moondalup_config.json" file
car_park = CarPark.from_config(config_file)

# TODO: create an entry sensor object with id 1, is_active True, and car_park car_park
entry_sensor = EntrySensor(Sensor_Id=1, Is_active=True, Car_park=car_park)

# TODO: create an exit sensor object with id 2, is_active True, and car_park car_park
exit_sensor = ExitSensor(Sensor_Id=2, Is_active=True, Car_park=car_park)

# TODO: create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
display = Display(display_Id=1, Message="Welcome to moondalup", Is_on=True, car_park=car_park)
car_park.register(entry_sensor)
car_park.register(exit_sensor)
car_park.register(display)

# TODO: drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
for _ in range(10):
    entry_sensor.detect_vehicle()

# TODO: drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)
for _ in range(2):
    exit_sensor.detect_vehicle()

