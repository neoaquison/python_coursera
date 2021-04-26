def primo(x):
    i = 2
    m = x // 2
    isprimo = True
    while i <= m:
        if x % i == 0:
            isprimo = False
        i += 1
    return isprimo

def maior_primo(x):
    i = 2
    maior = 0
    while i <= x:
        isprimo = primo(i)
        if isprimo:
            maior = i
        i += 1
    return maior

n = int(input("Digite um número: "))
print(maior_primo(n))
