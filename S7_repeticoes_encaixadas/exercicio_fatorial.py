# n = 1 
# while n > 0:
#     n = int(input("Digite umn número: "))
#     fatorial = 1
#     while n > 1:
#         fatorial = fatorial * n
#         n = n-1
#     print(f'Fatorial: {fatorial}')


def fator(n):
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n-1
    print(f'Fatorial: {fatorial}')

n = 1
while n > 0:
     n = int(input("Digite umn número: "))
     fator(n)
