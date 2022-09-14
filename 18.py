nord = 0
est = 1
sud = 2
ovest = 3
muovi = {nord: (0, 1), est: (1, 0), sud: (0, -1), ovest: (-1, 0)}
class Robot:
    def __init__(self, direzioni=nord, x=0, y=0):
        self.posiz = (x, y)
        self.direzioni = direzioni
    def move(self, movimento):
        for m in movimento:
            d, c = self.direzioni, self.posiz
            if m == "R":
                self.direzioni = d + 1 if d < 3 else 0
            elif m == "L":
                self.direzioni = d - 1 if d > 0 else 3
            elif m == "A":
                self.posiz = (c[0] + muovi[d][0], c[1] + muovi[d][1])