from pathlib import Path
from sensor import Sensor
from display import Display
from datetime import datetime
import json

class CarPark:
    def __init__(self, location = "Unknown", capacity = 100, log_file=Path("log.txt") ,plates =
    None, display = None, sensors = None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = display or []
        self.sensors = sensors or []
        self.log_file = Path(log_file)
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)

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
        self.Update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self,plate):
        self.plates.remove(plate)

    def Update_displays(self):
        for display in self.displays:
            display.update({"bays": self.available_bays})
            print(f"Car {display} updated.")

    @property
    def available_bays(self):
        #car_park.available_bays
        return max(0, self.capacity - len(self.plates))

    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    def log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now()}\n")

    def write_config(self):
        with open("config.json",
                  "w") as f:  # TODO: use self.config_file; use Path; add optional parm to __init__
            json.dump({"location": self.location,
                       "capacity": self.capacity,
                       "log_file": str(self.log_file)}, f)

    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])