class Display:
    def __init__(self, display_Id, car_park, Message="", Is_on=False, ):
        self.display_Id = display_Id
        self.Message = Message
        self.Is_on = Is_on
        self.car_park = car_park

    def __str__(self):
        return f"Display {self.display_Id}: {self.Message}"

    def update(self, Data):
        for key, value in Data.items():
            if hasattr(self, key):
                setattr(self, key, value)
