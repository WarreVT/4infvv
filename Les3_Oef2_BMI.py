gewicht = float(input("Hoeveel weeg je (in kg)? "))
lengte = float(input("Hoe groot ben je (in meter)? "))
BMI = gewicht / (lengte ** 2)
BMI = round(BMI, 1)
print(f"Je BMI is {BMI}. ")

if BMI < 18.5:
    print("Categorie: ondergewicht")

elif BMI < 25 and BMI >= 18.5:
    print("Categorie: gezond gewicht")

elif BMI < 30 and BMI >= 25:
    print("Categorie: overgewicht")

else:
    print("Categorie: zwaar overgewicht")