import math

class KvadRovnice:
    """ 
    Třída pro výpočet kvadratické rovnice v oboru reálných čísel
    """
    
    def __init__(self, a, b, c):
        """
        Konstruktor kvadratické rovnice

        a, b, c jsou reálná čísla

        ax^2 - kvadratický člen

        bx - lineární člen

        c - absolutní člen
        """
        self.a = a
        self.b = b
        self.c = c

    def diskriminant(self):
        """
        Výpočet diskriminantu

        D = b^2 - 4*a*c

        Mohou nastat 3 situace:

        D < 0 - rovnice nemá v oboru reálných čísel řešení

        D = 0 - rovnice má jeden dvojnásobný kořen

        D > 0 - rovnice má dva různé reálné kořeny
        """
        D = pow(self.b,2) - 4*self.a*self.c
        return D

    def vyres(self):
        """
        Výpočet kvadratické rovnice

        Mohou nastat 3 situace:

        D < 0 - rovnice nemá v oboru reálných čísel řešení

        D = 0 - rovnice má jeden dvojnásobný kořen
        
        D > 0 - rovnice má dva různé reálné kořeny

        Pro kořeny platí:

        x1 = (-b+sqrt(D))/(2*a)

        x2 = (-b-sqrt(D))/(2*a)

        Funkce vrací řetězec s popsaným výsledkem.
        """
        D = self.diskriminant()

        if D == 0:
            x = -self.b / (2 * self.a)
            textPopis = "Diskriminant je roven 0 a rovnice má jen jedno řešení: {}.".format(round(x,3))
            return(textPopis)
        
        elif D > 0:
            x1 = (-self.b + math.sqrt(D)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(D)) / (2 * self.a)
            textPopis = "Diskriminant je větší než 0 a rovnice má 2 řešení: {}, {}.".format(round(x1,3), round(x2,3))
            return(textPopis)
        
        else:
            textPopis = "Diskriminant je menší než 0 a rovnice nemá řešení v oboru reálných čísel."
            return(textPopis)

        
