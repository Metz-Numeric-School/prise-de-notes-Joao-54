FR = float(input("Note en français: "))
Math = float(input("Note en mathématiques: "))
Geo = float(input("Note en géographie: "))
Info = float(input("Note en informatique: "))

Moyenne = (FR + Math + Geo + Info) / 4

if (Moyenne >= 16 and Moyenne < 20):
    print("Moyenne:",Moyenne,"\nMention Très bien.")
elif (Moyenne >= 12 and Moyenne < 16):
    print("Moyenne:",Moyenne,"\nMention Bien.")
elif (Moyenne >= 8 and Moyenne < 12):
    print("Moyenne:",Moyenne,"\nMention Assez bien.")
elif (Moyenne >= 4 and Moyenne < 8):
    print("Moyenne:",Moyenne,"\nInsuffisant.")
elif (Moyenne >= 0 and Moyenne < 4):
    print("Moyenne:",Moyenne,"\nNul.")
else:
    print("Moyenne:",Moyenne)