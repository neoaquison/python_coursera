def primo(n):
    fator = 2
    while(n % fator != 0) and (fator <= n/2 ):
        fator = fator + 1
    if (n % fator != 0) or (n == 2):
        return True
    else:
        return False

def n_primos(n):
    i = 2
    count = 0
    fator = 2
    while(i <= n):
        if(primo(i)):
            count = count + 1
        i = i + 1
    return count

n = int(input('Digite um número inteiro:'))

print(n_primos(n))