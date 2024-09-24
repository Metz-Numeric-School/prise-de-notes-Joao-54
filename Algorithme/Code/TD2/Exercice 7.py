TTC = float(input("Saisissez un montant TTC: "))
Reduc = 0

if TTC >= 500 and TTC < 1000:
    Reduc = 2
elif TTC >= 1000 and TTC < 2000:
    Reduc = 5
elif TTC >= 2000:
    Reduc = 10
else:
    print("Le montant doit être de minimum 500 € pour avoir droit à une remise.")

if TTC>=2:
    nb1 = TTC * Reduc / 100
    Prix = TTC - nb1
    print("Une remise de",Reduc,"% a été appliquée, le nouveau montant à payer est de:",Prix,"€.")