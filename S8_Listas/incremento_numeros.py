n = int(input("Digite um número diferente de zero: "))
sequencia_digitada = []
aux = False
while not aux:
    while n != 0:
        sequencia_digitada.append(n)
        n = int(input("Digite um número diferente de zero: "))
        x = -1
    for i in range(len(sequencia_digitada)):        
        print(sequencia_digitada[x]) 
        x = x - 1       
        aux = True
