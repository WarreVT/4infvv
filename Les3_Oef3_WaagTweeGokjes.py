gok1 = int(input(" Raad een getal van 1 tot en met 10:"))
from random import randrange
geheim = (randrange(10) + 1)

if gok1 == geheim:
    print("Gewonnen in één keer!")
else:
    if gok1 < geheim:
        print("Hoger!")
    else:
        print("Lager!")
    gok2 = int(input("Raad nog een keer: "))
    if gok2 == geheim:
        print("Gewonnen bij je tweede gok!")
    else: 
        print("Helaas! Het getal was " + str(geheim))