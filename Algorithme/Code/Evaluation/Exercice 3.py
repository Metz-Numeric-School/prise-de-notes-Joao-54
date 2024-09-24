print("================ DÉBUT PROGRAMME ================\n\n")
nb1 = float(input("Entrez un premier nombre: "))
nb2 = float(input("Entrez un deuxième nombre: "))

print("La somme de",nb1,"et",nb2,"est",nb1+nb2)

if nb1>nb2:
    print("La différence entre",nb1,"et",nb2,"est",nb1-nb2)
else:
    print("La différence entre",nb1,"et",nb2,"est",nb2-nb1)

print("Le produit de",nb1,"par",nb2,"est",nb1*nb2)

if nb2!=0:
    print("Le quotient de",nb1,"et",nb2,"est",nb1/nb2)
else:
    print("Erreur: division par zéro.")
print("\n\n================ FIN PROGRAMME ================")