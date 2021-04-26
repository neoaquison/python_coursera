n = int(input('Digite o valor de n: '))
anterior = n

if n == 0:
    fatorial = 1
else:
    while n > 0:
        fatorial = anterior
        resto = n - 1 
        produto = fatorial * resto
        anterior = produto
        n = resto
print(f'{fatorial}')
