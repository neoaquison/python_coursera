numero = int(input('Digite o primeiro número: '))

resto = numero % 10
numero = numero // 10
adj_iguais = False

while numero > 0 and not adj_iguais:
    num_atual = numero % 10
    if num_atual == resto:
        adj_iguais = True
    else:
        resto = num_atual
        numero = numero // 10
if adj_iguais:
    print("Há números adjacentes iguais na sequencia")
else:
    print('Não tem números adjacentes iguais na sequencia')
