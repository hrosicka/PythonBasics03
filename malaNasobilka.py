from random import randrange

print ("Malá násobilka")
print ("--------------")
print ("Program náhodně vygeneruje 2 čísla od 1 do 10")
print ("Znáš výsledek?")

cislo1 = randrange(0,10)
cislo2 = randrange(0,10)

print ("Byla vybrána číslo {} a {}".format(cislo1, cislo2))
print ("Kolik je {} x {}?".format(cislo1, cislo2))

spravnyVysledek = cislo1 * cislo2

while True:
        vysledek = input()
        try:
            uzivatelskyVysledek = int(vysledek)
            break
        except ValueError:
            print("Zadaná hodnota není číslo! Zkus to znovu!") 

if spravnyVysledek == uzivatelskyVysledek:
    print("Jupí! Umíš počítat!")
else:
    print("Zkus ještě trénovat! Správný výsledek je {}.".format(spravnyVysledek))
