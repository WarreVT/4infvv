getal = int(input(" Raad een getal van 1 tot en met 10:"))
from random import randrange
geheim = (randrange(10) + 1)

if getal == geheim:
    print("Gewonnen! Het getal was " + str(getal))

if getal != geheim:
    print("Helaas! Het getal was " + str(geheim))
