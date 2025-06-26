class CarPark:
    def __init__(self, location = "Unknown", capacity = 100, plates = None, display = None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.display = display or []

    def __str__(self):
