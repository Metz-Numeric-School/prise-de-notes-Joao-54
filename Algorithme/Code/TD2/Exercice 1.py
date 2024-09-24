FR = float(input("Note en français: "))
FR1 = float(input("Coefficient français: "))
Math = float(input("Note en mathématiques: "))
Math1 = float(input("Coefficient mathématiques: "))
Geo = float(input("Note en géographie: "))
Geo1 = float(input("Coefficient géographie "))
Info = float(input("Note en informatique: "))
Info1 = float(input("Coefficient informatique "))

somme1 = (FR*FR1) + (Math*Math1) + (Geo*Geo1) + (Info*Info1)
somme2 = FR1 + Math1 + Geo1 + Info1
Moyenne = somme1/somme2
print("La moyenne de l'élève est de",Moyenne)