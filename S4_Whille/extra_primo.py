numero = int(input('Digite um número inteiro: '))
metade = numero / 2

while metade > 1:
    multiplo = metade -1
    if metade % multiplo == 0:
        print('não primo')
    else:
        print('primo')
    metade = metade -1
