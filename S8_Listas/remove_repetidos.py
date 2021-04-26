def remove_repetidos(lista):
    anterior = 0
    s_repetidos = []
    contagem = len(lista)
    for i in range(len(lista)):
        anterior = lista[i]
        if anterior in s_repetidos:
            anterior = anterior
        else:
            s_repetidos.append(lista[i])
    s_repetidos = sorted(s_repetidos)
    return s_repetidos


def lista():
    n = int(input("Digite um número maior do que zero: "))
    lista = []

    while n >= 0:
        lista.append(n)
        n = int(input("Digite um número maior do que zero: "))

    print(remove_repetidos(lista))

lista()