largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

aux_largura = largura

while altura > 0:
    while largura > 0:
        print('#', end="")
        largura = largura -1
    print()
    largura = aux_largura
    altura = altura -1
