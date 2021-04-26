import math

def delta(a,b, c):
    return (b ** 2) - (4 * a * c)
    
def raiz1(b, delta, a):
    return (- b + math.sqrt(delta)) / (2 * a)
    
def raiz2(b, delta, a):
    return (- b - math.sqrt(delta)) / (2 * a)
def main():
    a = float(input('Digite o valor de a: '))
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))
    retorna_variaveis(a, b, c)

def retorna_variaveis(a, b, c):
    delta = delta(a,b, c)

    if delta < 0:
        print('Não existe raiz real')
    elif delta == 0:
        r1 =  raiz1(b, delta, a)
        print(f'Só existe uma raiz real x1 = {r1}')
    else:
        r1 =  raiz1(b, delta, a)
        r2 =  raiz1(b, delta, a)
        print(f'Existem duas raizes reais x1 = {r1} e x2 = {r2}')
main()