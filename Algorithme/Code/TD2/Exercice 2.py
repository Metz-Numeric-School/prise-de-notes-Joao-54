nb1 = float(input("Saisir un premier nombre: "))
nb2 = float(input("Saisir un deuxième nombre: "))
nb3 = float(input("Saisir un troisième nombre: "))

if nb1 <= nb2 and nb2 <= nb3:
    print("Les nombres sont triés en ordre croissant.")
else:
    print("Les nombres ne sont pas triés en ordre croissant.")