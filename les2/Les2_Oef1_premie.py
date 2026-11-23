getal1 = float(input("Hoeveel euro betaalde je voor je zonnenpanelen? "))
premie = float(getal1/5)
max_premie = float(600)

if premie >= 600:
    print(f"Je krijgt een premie van {max_premie} euro.")

if premie < 600:
    print(f"Je krijgt een premie van {premie} euro.")
