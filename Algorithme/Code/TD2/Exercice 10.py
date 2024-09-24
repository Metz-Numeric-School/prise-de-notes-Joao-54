amb = float(input("Saisissez la température ambiante: "))
ref = float(input("Saisissez la température des bassins de refroidissement: "))
dif = 0

if amb >= ref:
    dif = amb - ref
else:
    dif = ref - amb

if (dif < 20 or dif > 40):
    print("L'alarme retentit! La différence est de",dif,"°C.")
else:
    print("La différence est de",dif,"°C. Rien à signaler.")