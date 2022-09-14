class Matrix(object):
    def __init__(self, stringa):
        self.matrix = [[int(i) for i in e.split()] for e in stringa.split("\n")]
    def row(self, x):
        return self.matrix[x - 1]
    def column(self, x):
        return [r[x - 1] for r in self.matrix]