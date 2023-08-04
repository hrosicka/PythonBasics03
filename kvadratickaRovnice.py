class KvadRovnice:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def determinant(self):
        D = pow(self.b,2) - 4*self.a*self.c
        return D

    def vyres(self):

        D = self.determinant()

        if D == 0:
            x = -self.b / (2 * self.a)
            textPopis = "Determinant je roven 0 a rovnice má jen jedno řešení: {}.".format(x)
            return(textPopis)
        
