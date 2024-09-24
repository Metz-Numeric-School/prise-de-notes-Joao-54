print("a x + b = 0")
a = float(input("Entrer le nombre a: "))
b = float(input("Entrer le nombre b: "))

print(a,"x +",b,"-",b,"=","0 -",b)
b = 0-b
print(a,"x =",b)

print("x =",b,"/",a)

if (a==0 and b==0):
    print("\nL'ensemble des solutions est l'ensemble R.")
elif (a== 0 and b!=0):
    print("\nL'ensemble des solutions est l'ensemble vide.")
elif a!=0:
    print("La solution est",b,"/",a)