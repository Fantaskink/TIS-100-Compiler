class Register:

    def __init__(self, name, index):
        self.name = name
        self.index = index

    def get_string(self):
        return "X" + str(self.index)
