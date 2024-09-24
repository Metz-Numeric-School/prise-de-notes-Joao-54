print("================ DÉBUT PROGRAMME ================\n\n")
nb1 = int(input("Entrez un premier nombre entier: "))
nb2 = int(input("Entrez un deuxième nombre entier: "))
nb3 = nb1/nb2

if nb1 > nb2:
    print(nb1,"est supérieur à",nb2)
else:
    print(nb1,"est inférieur à",nb2)

if nb1 == nb2:
    print(nb1,"est égal à",nb2)

if nb3%2 == 0:
    print(nb1,"est divisible par",nb2)
print("\n\n================ FIN PROGRAMME ================")
