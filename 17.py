ore = 24
minuti = 60
class Orologio:
    def __init__(self, ore, minuti):
        self.minuti = 0
        minuti = minuti + (ore % ore) * minuti
        self.__add__(minuti)
    def tempo(self):
        tuple = divmod(self.minuti, minuti)
        return (tuple[0] % ore, tuple[1])
    def __repr__(self):
        return f"Orologio({self.tempo()[0]}, {self.tempo()[1]})"
    def __str__(self):
        return f"{self.tempo()[0]:02d}:{self.tempo()[1]:02d}"
    def __eq__(self, other):
        return self.tempo() == other.tempo()
    def __add__(self, minuti):
        self.minuti += minuti
        return str(self)
    def __sub__(self, minuti):
        self.minuti -= minuti
        return str(self)