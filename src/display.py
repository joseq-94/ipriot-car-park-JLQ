class Display:
    def __init__(self, Id, Message="", Is_on=False):
        self.Id = Id
        self.Message = Message
        self.Is_on = Is_on

    def __str__(self):
        return f"Display {self.Id}: {self.Message}"