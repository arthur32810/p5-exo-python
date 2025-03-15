## Écrivez votre code ici !
def square(nombre):
    if nombre.isdigit():
        return int(nombre) ** 2
    else:
        print("Le paramètre n'est pas un nombre !")
        return None


number = input("Saisissez un nombre :")
result = square(number)
print(result)
