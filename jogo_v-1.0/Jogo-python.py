from random import choice
import os
from time import sleep

pontos = ini = 0
esportes = ['Quem é PELÉ ?', 'Quem é CR7?',
            'Goleada começa com __ gols.!', 'Um jogo tem __ minutos',
            'Ganha __ pontos com um empate', 'Ganha __ pontos com a vitoria']
musica = ("'Evidencias ' - pertece a dupla...", 'David Bowie apareceu em que filme cult em 1986? ',
          'De que país vem o icônico trio pop A-ha? ', 'Huey, de Huey Lewis and the News, tocou qual instrumento?',
          '"Dilemma" pertence ao cantor e a cantora.. ', 'Com quantos anos Michael Jackson iniciou a carreira?')
comida = ('Qual programa de culinaria é o que tem mais audencia ?', 'Bolacha ou Biscoito ?',
          'De onde veio o pão de queijo', 'Sabor 4 queijos geralmente é ..',
          "qual significado de '\033[30;44mWEDDING CAKE\033[m' ?", 'Tem barba mas não é homem,'
                                                                   'Tem dente mas não é gente')
novela = ('Qual nome da protagonista da novela MariMar ?', 'Lupita é uma personagem de qual novela ?',
          'Em Carrossel, Cirilo gosta de qual colega ?', 'Qual nome do pai de Tati e Vivi em Chiquititas ?',
          'Gabriela E.S Utrera é a protagonista de qual novela? ', 'Qual dessas é uma novela de 1990?')
bebidas = ('Qual porcentagem de alcool de uma cerveja comum', 'Qual destes não está presente no yogurt',
           '"O café é eficaz contra o sono", essa afirmativa está ...', 'O vinho é feito a partir de qual fruta?',
           'A coca-cola pode fazer mal por ser muito ...', 'Qual bebida mais forte e mais fraca, respectivamente ?')


def menu():
    print('\033[33m     Temas \033[m')
    temas = ('| 0 - Sair',
             '| 1 - Esportes',
             '| 2 - Musica',
             '| 3 - Comida',
             '| 4 - Novela',
             '| 5 - Bebidas'
             )
    print('\033[34m -' * 10)
    for item in temas:
        print(f'\033[93m{item:<20}|', '\033[34m')
        sleep(0.5)
    print(' -' * 10, '\033[m')


while True:
    print("\033[36mpress 'GO' to enter")
    inicio = input().upper().strip()
    while inicio not in 'GO':
        inicio = input("\033[31mErro...\033[36mpress 'GO' to enter \n").upper().strip()
    os.system('cls') or None
    if inicio in 'GO':
        try:
            menu()
            while True:
                opcao = int(input('Sua escolha: '))
                while opcao > 5 or opcao < 0:
                    opcao = int(input('\033[31mErro..\033[mSua escolha: \n'))
                if opcao == 0:
                    break

                elif opcao == 1:
                    p = choice(esportes)
                    print(p)
                    if p == esportes[0]:
                        print('A - Rei do futebol'
                              '\nB - Chapeleiro Maluco '
                              '\nC - Presidente da Venezuela')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'Aa':

                            print('Você \033[32mACERTOU\033[m')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU\033[m')
                    elif p == esportes[1]:
                        print('A - Ronaldo Fenomeno'
                              '\nB - Cristiano Ronaldo '
                              '\nC - Ciquinho Scarpa')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'Bb':
                            print('Você \033[32mACERTOU')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU')
                    elif p == esportes[2]:
                        print('A - 5 gols '
                              '\nB - 4 gols'
                              '\nC - 3 gols')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'Bb':
                            print('Você \033[32mACERTOU')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU')
                    elif p == esportes[3]:
                        print('A - 90 '
                              '\nB - 120'
                              '\nC - 45')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'Aa':
                            print('Você \033[32mACERTOU')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU')
                    elif p == esportes[4]:
                        print('A - 2'
                              '\nB - 5'
                              '\nC - 1')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'Cc':
                            print('Você \033[32mACERTOU')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU')
                    elif p == esportes[5]:
                        print('A - 7'
                              '\nB - 3'
                              '\nC - 2.5')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'bB':
                            print('Você \033[32mACERTOU')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU')
                    sleep(3)
                    os.system('cls') or None

                elif opcao == 2:
                    p = choice(musica)
                    print(p)
                    if p == musica[0]:
                        print('A - Paulo e Palinho'
                              '\nB - Maiara e Maraisa'
                              '\nC - Chitãozinho & Xororó')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'cC':
                            print('Você \033[32mACERTOU\033[m')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU\033[m')
                    elif p == musica[1]:
                        print('A - Onde está segunda?'
                              '\nB - Labirinto'
                              '\nC - Velozes e Furiosos')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'bB':
                            print('Você \033[32mACERTOU\033[m')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU\033[m')
                    elif p == musica[2]:
                        print('A - Brasil'
                              '\nB - Noruega'
                              '\nC - Xangai')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'bB':
                            print('Você \033[32mACERTOU\033[m')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU\033[m')
                    elif p == musica[3]:
                        print('A - Gaita'
                              '\nB - Violino'
                              '\nC - Berimbau')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'aA':
                            print('Você \033[32mACERTOU\033[m')

                            pontos += 1
                        else:
                            print('Você \033[31mERROU\033[m')
                    elif p == musica[4]:
                        print('A - MariMar'
                              '\nB - Sandi & Junior'
                              '\nC - Nelly & Kelly')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'cC':
                            print('Você \033[32mACERTOU\033[m')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU\033[m')
                    elif p == musica[5]:
                        print('A - 32'
                              '\nB - 19'
                              '\nC - 5')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'Cc':
                            print('Você \033[32mACERTOU\033[m')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU\033[m')
                    sleep(3)
                    os.system('cls') or None

                elif opcao == 3:
                    p = choice(comida)
                    print(p)
                    if p == comida[0]:
                        print('A - Que Seja Doce'
                              '\nB - Bake Off'
                              '\nC - Master Chef')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'cC':
                            print('Você \033[32mACERTOU\033[m')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU\033[m')
                    elif p == comida[1]:
                        print('A - Os 2'
                              '\nB - Bixcoito'
                              '\nC - Pão de queijo')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'aA':
                            print('Você \033[32mACERTOU\033[m')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU\033[m')
                    elif p == comida[2]:
                        print('A - Minas Gerais'
                              '\nB - Rondonia'
                              '\nC - Roma')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'aA':
                            print('Você \033[32mACERTOU\033[m')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU\033[m')
                    elif p == comida[3]:
                        print('A - de Refrigerante'
                              '\nB - de Pizza'
                              '\nC - de Bolo')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'bB':
                            print('Você \033[32mACERTOU\033[m')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU\033[m')
                    elif p == comida[4]:
                        print('A - Macarrão na chapa'
                              '\nB - Bolo de Casamento'
                              '\nC - Carne de boi')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'bB':
                            print('Você \033[32mACERTOU\033[m')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU\033[m')
                    elif p == comida[5]:
                        print('A - Feijão'
                              '\nB - Cebola'
                              '\nC - Alho')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'cC':
                            print('Você \033[32mACERTOU\033[m')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU\033[m')
                    sleep(3)
                    os.system('cls') or None

                elif opcao == 4:
                    p = choice(novela)
                    print(p)
                    if p == novela[0]:
                        print('A - Anita'
                              '\nB - Ariadna Thalía Sodi Miranda Mottola '
                              '\nC - Jacqueline Chantal Fernández Andere Rivero')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'bB':
                            print('Você \033[32mACERTOU\033[m')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU\033[m')
                    elif p == novela[1]:
                        print('A - Rebelde'
                              '\nB - Malhação'
                              '\nC - carinha de Anjo')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'aA':
                            print('Você \033[32mACERTOU\033[m')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU\033[m')
                    elif p == novela[2]:
                        print('A - Maria Joaquina'
                              '\nB - Valeria'
                              '\nC - Dona Florinda')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'aA':
                            print('Você \033[32mACERTOU\033[m')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU\033[m')
                    elif p == novela[3]:
                        print('A - Roberto'
                              '\nB - Carlos '
                              '\nC - Cícero')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'cC':
                            print('Você \033[32mACERTOU\033[m')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU\033[m')
                    elif p == novela[4]:
                        print('A - Maria do Bairro '
                              '\nB - Rei do Gado'
                              '\nC - A Usurpadora')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'cC':
                            print('Você \033[32mACERTOU\033[m')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU\033[m')
                    elif p == novela[5]:
                        print('A - Rei do Gado'
                              '\nB - Terra Nostra'
                              '\nC - Eta Mundo Bão')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'bB':
                            print('Você \033[32mACERTOU\033[m')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU\033[m')
                    sleep(3)
                    os.system('cls') or None

                elif opcao == 5:
                    p = choice(bebidas)
                    print(p)
                    if p == bebidas[0]:
                        print('A - 4.5%'
                              '\nB - 7%'
                              '\nC - 3.45%')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'aA':
                            print('Você \033[32mACERTOU\033[m')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU\033[m')
                    elif p == bebidas[1]:
                        print('A - Açucar'
                              '\nB - Conservantes'
                              '\nC - Glutém')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in '':
                            print('Você \033[32mACERTOU\033[m')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU\033[m')
                    elif p == bebidas[2]:
                        print('A - Correta'
                              '\nB - Incorreta'
                              '\nC - Incompleta')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'cC':
                            print('Você \033[32mACERTOU\033[m')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU\033[m')
                    elif p == bebidas[3]:
                        print('A - Uva'
                              '\nB - Guaraná'
                              '\nC - Maracuja')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'Aa':
                            print('Você \033[32mACERTOU\033[m')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU\033[m')
                    elif p == bebidas[4]:
                        print('A - Doce'
                              '\nB - Salgada'
                              '\nC - Amarga')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'Aa':
                            print('Você \033[32mACERTOU\033[m')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU\033[m')
                    elif p == bebidas[5]:
                        print('A - Wisky & Cerveja Pilsen'
                              '\nB - Vinho & SkolBeats'
                              '\nC - Cocoroco & Hard Seltzer')
                        res = input('Alternativa: ').upper().strip()[0]
                        while res not in 'ABC':
                            res = input('\033[31mErro...\033[mAlternativa: ').upper().strip()[0]
                        if res in 'cC':
                            print('Você \033[32mACERTOU\033[m')
                            pontos += 1
                        else:
                            print('Você \033[31mERROU\033[m')
                    sleep(3)
                    os.system('cls') or None

                else:
                    print('Valor incorreto, tente novamente')
                ini += 1
                cont = str(input('\033[mContinuar ?\033[34m[S/N] \033[m')).strip().upper()[0]
                while cont not in 'SsNn':
                    cont = str(input('\033[31mError...\033[mContinuar ?[S/N] ')).strip().upper()[0]
                if cont in 'Ss':
                    menu()
                else:
                    break
                os.system('cls') or None
        except ValueError or TypeError or IndexError:
            print('\033[31mErro.. Tente novamente')
    break


if ini == 0:
    print('Que pena não ter jogado...')
elif ini >= 1:
    print('Gostou de ter jogado ? Se sim, joga denovo ai..(;')
if pontos <= 1:
    print(f'\033[35mVocê obteve um total de \033[30m{pontos}\033[35m acerto')
elif pontos > 1:
    print(f'\033[35mVocê obteve um total de \033[30m{pontos}\033[35m acertos')



