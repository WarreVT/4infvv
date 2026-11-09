from random import randrange
geheim1 = (randrange(10) + 1)
from random import randrange
geheim2 = (randrange(10) + 1)
print(int(input("Hoeveel is " + str(geheim1) + "x" + str(geheim2) + "?" )))
if int(input("Hoeveel is " + str(geheim1) + "x" + str(geheim2) + "?")) == geheim1 * geheim2: