class PunteggioMassimo:
    def __init__(self, punti):
        
        self.punti = punti
    
    def ultimo(self):
        
        return self.punti[-1]
    def migliore(self):
        return max(self.punti)
    def megliodeitre(self):
        copy = self.punti.copy()
        top = PunteggioMassimo(copy).migliore()
        copy.remove(top)
        if (len(copy) == 0):
            return [top]
        top2 = PunteggioMassimo(copy).migliore()
        copy.remove(top2)
        if (len(copy) == 0):
            return [top, top2]
        
        top3 = PunteggioMassimo(copy).migliore()
        return [top, top2, top3]