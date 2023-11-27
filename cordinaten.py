



class Cordinaaten():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_16 = self.x // 16
        self.y_16 = self.x // 16
        self.x_7 = self.x // 7
        self.y_7 = self.x // 7

    def update(self):
        self.x_16 = self.x // 16
        self.y_16 = self.x // 16
        self.x_7 = self.x // 7
        self.y_7 = self.x // 7

