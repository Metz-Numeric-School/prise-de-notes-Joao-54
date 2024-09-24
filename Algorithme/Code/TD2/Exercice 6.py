HT = float(input("Saisir le prix HT du produit: "))
TVA = int(input("Pour une TVA de 5,5% - Saisissez 1\nPour une TVA de 19,6% - Saisissez 2\nPour une TVA de 33% - Saisissez 3\n"))

if TVA == 1:
    TVA = 5.5
elif TVA == 2:
    TVA = 19.6
elif TVA == 3:
    TVA = 33
else:
    print("Erreur, veuillez choisir parmis les trois options.")

Prix = HT + (HT*TVA/100)

print("Le prix HT est de",HT,"€, la TVA est de",TVA,"% et le prix TTC est de",Prix,"€.")