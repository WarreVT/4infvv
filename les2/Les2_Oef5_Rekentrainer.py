from random import randrange
geheim1 = (randrange(10) + 1)
from random import randrange
geheim2 = (randrange(10) + 1)
if int(input("Hoeveel is " + str(geheim1) + "x" + str(geheim2) + "?")) == geheim1 * geheim2:
    print("Juist, goed zo!")
else:
    print("Fout! Het juiste antwoord is " + str(geheim1 * geheim2) + ".")