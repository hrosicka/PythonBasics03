
from random import randint

print("HRA: OKO BERE")
print("-------------")

sum = 0

while sum < 21:
    print("Máš {} bodu".format(sum))
    odpoved = 0
    while (odpoved != "ano"):
        odpoved = input("Otočit kartu [ano/ne]")
        odpoved = odpoved.lower()
        if odpoved == "ano":
            karta = randint(2,10)
            print(karta)
            sum = sum + karta
            print(sum)
        elif odpoved == "ne":
            break
    if (odpoved == "ne"):
        break


if sum == 21:
    print("Gratuluji! Vyhrál/a jsi!")
elif sum > 21:
    print("Smůla! {} bodů je moc!".format(sum))
else:
    print("Chybělo jen {} bodů!".format(21-sum))
