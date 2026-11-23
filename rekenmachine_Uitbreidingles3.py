import math
getal1 = float(input("Geef getal 1: "))
getal2 = float(input("Geef getal 2: "))
bewerking = input("Welke bewerking wil je uitvoeren (+,-,/,*,m,w): ")

if bewerking == "+":  #== : is gelijk aan ; <= : kleiner dan en gelijk aan ; < : kleiner dan; != : niet gelijk aan
    print(f"{getal1} + {getal2} = {getal1+getal2}")

elif bewerking == "-":
    print(f"{getal1} - {getal2} = {getal1-getal2}")

elif bewerking == "/":
    if getal2 == 0:
        print("Delen door nul kan niet!")
    else:
        print(f"{getal1} / {getal2} = {getal1/getal2}")
    

elif bewerking == "*":
    print(f"{getal1} * {getal2} = {getal1*getal2}")

elif bewerking == "m":
    print(f"{getal1} tot de {getal2}e macht = {getal1**getal2}")

elif bewerking =="w":
    print("De wortel van " + str(getal1) + " is " + str(math.sqrt(getal1)))

else:
    print("Deze bewerking ken ik niet.")


