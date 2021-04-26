def vogal(x):
    x = x.lower()
    vog = False
    if x == "a":
        vog = True
    elif x == "e":
        vog = True
    elif x == "i":
        vog = True
    elif x == "o":
        vog = True
    elif x == "u":
        vog = True

    return vog

letra = input("Digite uma letra: ")

print(vogal(letra))
