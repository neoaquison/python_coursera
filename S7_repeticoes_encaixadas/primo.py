def ePrimo(n):
    fator = 2 

    if n == 2:
        return True

    else:
        while n % fator != 0 and fator <= n/2:
            fator = fator + 1
        if n % fator == 0:
            return False
        else:
            return True


n = int(input('Digite um número inteiro:'))

while n > 0:
    if ePrimo(n):
        print(f'{n} é primo!')
    else:
        print(f'{n} não é primo!')
        
    n = int(input('Digite um número inteiro:'))