class Register:

    def __init__(self, index):
        self.index = index

    def get_string(self):
        return "X" + str(self.index)
