HT = float(input("Entrer le prix unitaire HT: "))
QT = int(input("Entrer la quantité: "))

total = HT*QT
print("Le prix total HT pour ces articles est de",total,"euros.")

R1 = total*0.85
print("On applique la remise de 15% et on obtient un prix de",R1,"euros.")

TVA = int(input("Entrer le taux de TVA: "))
R2 = R1 + (R1*TVA/100)

print("En appliquant maintenant la TVA, on a un prix final de",R2,"euros.")
