from kvadratickaRovnice import *


def main():

    print("KVADRATICKÁ ROVNICE")
    print("-------------------")

    while True:
            cislo1 = input("Zadejte koeficient a: ")
            try:
                a = float(cislo1)
                break
            except ValueError:
                print("Zadaná hodnota není číslo! Zkus to znovu!")     

    while True:
            cislo2 = input("Zadejte koeficient b: ")
            try:
                b = float(cislo2)
                break
            except ValueError:
                print("Zadaná hodnota není číslo! Zkus to znovu!")

    while True:
            cislo3 = input("Zadejte koeficient c: ")
            try:
                c = float(cislo3)
                break
            except ValueError:
                print("Zadaná hodnota není číslo! Zkus to znovu!")


    KV1 = KvadRovnice(a, b, c)
    print(KV1.vyres())



if __name__ == "__main__":
    main()