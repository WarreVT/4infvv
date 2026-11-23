from datetime import date
huidig_jaar = date.today().year

GeboorteJaar = int(input("In welk jaar ben je geboren? "))

Leeftijd = huidig_jaar - GeboorteJaar
print(f"Dit jaar word je {Leeftijd} jaar.")

if Leeftijd < 12:
    print("Je mag naar films voor alle leeftijden.")

elif Leeftijd < 16:
    print("Je mag naar films vanaf 12 jaar.")

elif Leeftijd < 18: 
    print("Je mag naar films vanaf 16 jaar.")

else:
    print("Je mag naar alle films.")