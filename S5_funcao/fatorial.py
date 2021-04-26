def fatorial(n):
    anterior = n
    if n == 0:
        return 1
    else:
        while n > 0:
            fatorial = anterior
            resto = n - 1 
            produto = fatorial * resto
            anterior = produto
            n = resto
        return fatorial

n = int(input('Digite o valor de n: '))
k = int(input('digite o valor de k: '))

fatn = fatorial(n)
print(fatn)
fatk = fatorial(k)
fatnk = fatorial(n-k)
newton = fatn / (fatk * fatnk)

print(f'Coeficiente binoomial é: {newton}')
