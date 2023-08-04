import math
class KvadRovnice:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # výpočet determinantu
    def determinant(self):
        D = pow(self.b,2) - 4*self.a*self.c
        return D

    # řešení kvadratické rovnice podle výsledku determinantu
    def vyres(self):
        D = self.determinant()

        if D == 0:
            x = -self.b / (2 * self.a)
            textPopis = "Determinant je roven 0 a rovnice má jen jedno řešení: {}.".format(round(x,3))
            return(textPopis)
        
        elif D > 0:
            x1 = (-self.b + math.sqrt(D)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(D)) / (2 * self.a)
            textPopis = "Determinant je větší než 0 a rovnice má 2 řešení: {}, {}.".format(round(x1,3), round(x2,3))
            return(textPopis)
        
        else:
            textPopis = "Determinant je menší než 0 a rovnice nemá řešení v oboru reálných čísel."
            return(textPopis)

        
