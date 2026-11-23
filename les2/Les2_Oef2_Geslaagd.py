Score = int(input("Hoeveel punten heb je behaald? "))
Totaal = int(input(" Op hoeveel punten stond de toets? "))
Percentage = float(Score / Totaal * 100)
Percentage = round(Percentage, 1)
print(" Je hebt " + str(Percentage) + "%.")
if Percentage >= 50:
    print("Proficiat, je bent geslaagd!")

if Percentage < 50:
    print("Jammer, je bent niet geslaagd.")
