largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

aux_largura = largura
aux_altura = altura

while altura > 0:
    if altura == 1:
        while largura > 0:
            print('#', end="")
            largura = largura -1
    elif altura == aux_altura:
         while largura > 0:
            print('#', end="")
            largura = largura -1
    else:
        while largura > 0:
            if largura == aux_largura:
                print('#', end="")
                largura = largura -1
            elif largura == 1:
                print('#', end="")
                largura = largura -1
            else:            
                while largura > 1:
                    print(' ', end="")
                    largura = largura -1
    print()
    largura = aux_largura
    altura = altura -1
