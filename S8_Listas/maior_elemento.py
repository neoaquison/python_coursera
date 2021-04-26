def maior_elemento(lista):
    anterior = 0
    contagem = len(lista)
    for i in range(len(lista)):
        if anterior > lista[i]:
            anterior = anterior
        else:
            if i == contagem:
                anterior
            else:
                anterior = lista[i]
    return anterior

def lista():
    n = int(input("Digite um número maior do que zero: "))
    lista = []

    while n >= 0:
        lista.append(n)
        n = int(input("Digite um número maior do que zero: "))

    print(maior_elemento(lista))

lista()