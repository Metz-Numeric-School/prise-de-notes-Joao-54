nb1 = int(input("Nombre de doigts du joueur A: "))
nb2 = int(input("Nombre de doigts du joueur B: "))
nb3 = nb1 + nb2

if nb3%2==0:
    print("Le joueur A a gagné.")
else:
    print("Le joueur B a gagné.")