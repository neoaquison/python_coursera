def computador_escolhe_jogada(n, m):
    computador_retira = 1

    while computador_retira != m:
        if (n - computador_retira) % (m+1) == 0:
            return computador_retira
        else:
            computador_retira = computador_retira +1
    return computador_retira

def usuario_escolhe_jogada(n, m):
    jogo_certo = False

    while jogo_certo != True:
        usuario_retira = int(input('Quantas peças você vai tirar? ' ))
        if usuario_retira > m or usuario_retira <1:            
            print('\nOops! Jogada inválida! Tente de novo.\n')
        else:
            jogo_certo = True
    return usuario_retira

def partida():
    n = int(input('Quantas peças? ' ))
    m = int(input('Limite de peças por jogada? ' ))
    jogada_computador = False

    if n % (m+1) == 0:
        print('\nVoce começa!')
    else:
        print('\nComputador começa!\n')
        jogada_computador = True

    while n > 0:
        if jogada_computador != False:
            computador_retira = computador_escolhe_jogada(n, m)
            n = n - computador_retira
            if computador_retira == 1:
                print('O computador tirou uma peça.')
            else:
                print(f'O computador tirou {computador_retira} peças.\n')
            jogada_computador = False
        else:
            usuario_retira = usuario_escolhe_jogada(n, m)
            n = n - usuario_retira
            if usuario_retira == 1:
                print('\nVocê tirou uma peça.')
            else:
                print(f'\nVocê tirou {usuario_retira} peças.')
            jogada_computador = True
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.\n')
        else:
            print(f'Agora restam {n} peças no tabuleiro.\n')

    print('Fim do jogo! O computador ganhou!\n')

def campeonato():
    rodada = 1
    while rodada <= 3:
        print(f'**** Rodada {rodada} ****\n')
        partida()
        rodada = rodada + 1
    print('**** Final do campeonato! ****')
    print('\nPlacar: Você 0 X 3 Computador')

print('\nBem-vindo ao jogo do NIM! Escolha:\n')
print('1 - para jogar uma partida isolada')
num_partidas = int(input('2 - para jogar um campeonato '))

if num_partidas == 2:
    print('\nVoce escolheu um campeonato!\n')
    campeonato()
elif num_partidas == 1:
    print('\n')
    partida()