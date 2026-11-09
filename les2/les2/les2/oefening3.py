seconden = int(input("Hoeveel seconden tel je tussen bliksem en donder?:"))
afstand = float(seconden * 343 / 1000)
afstand = round(afstand, 1)
print( "Het onweer is ongeveer " + str(afstand) + " km ver.")
if afstand < 3:
    print("Opgelet! Het onweer is dichtbij. Ga snel naar binnen!")