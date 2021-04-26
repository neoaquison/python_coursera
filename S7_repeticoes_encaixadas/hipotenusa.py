def soma_hipotenusas(n):
    soma = 1
    hipo = 0
    while soma <= n:
        if é_hipotenusa(soma):
            hipo = hipo + soma
        soma = soma + 1
    return hipo

def é_hipotenusa(n):
    from math import sqrt
    ca = 1
    co = 1
    hipo = False
    while ca <= n and not hipo:
        while co <= n and not hipo:
            hipotenusa = sqrt(ca ** 2 + co ** 2)
            if n == hipotenusa:
                hipo = True
            co = co + 1
        co = 1
        ca = ca +1
    return hipo
    
def main():
    n = int(input('Hipotenusa: '))
    print(soma_hipotenusas(n))
    
main()