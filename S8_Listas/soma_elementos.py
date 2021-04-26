def soma_elementos(lista):
    soma = 0

    for i in range(len(lista)):
        soma = lista[i] + soma
        
    return soma

def lista():
    n = int(input("Digite um número maior do que zero: "))
    lista = []

    while n >= 0:
        lista.append(n)
        n = int(input("Digite um número maior do que zero: "))

    print(soma_elementos(lista))

lista()