class Display:
    def __init__(self, Display_Id, Message="", Is_on=False):
        self.Display_Id = Display_Id
        self.Message = Message
        self.Is_on = Is_on

    def __str__(self):
        return f"Display {self.Display_Id}: {self.Message}"

    def update(self, Data):
        for key, value in Data.items():
            print(f"{key}: {value}")