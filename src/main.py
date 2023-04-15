import mysql.connector as mysql
import lib.interface as interface
from tabulate import tabulate
from time import sleep
from tqdm import tqdm
import os

conexao = mysql.connect(
    host='us-cdbr-east-06.cleardb.net',
    user='b1e1246e0d4eed',
    password='dcd8e79b',
    database='heroku_25b7ace0ee7f569',
)

cursor = conexao.cursor()


def limpa_amostras():
    global mp10
    global mp25
    global o3
    global co
    global no2
    global so2

    mp10 = None
    mp25 = None
    o3 = None
    co = None
    no2 = None
    so2 = None


def limpa_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def imprimir_tabulado(amostras, headers):
    print('Amostras cadastradas:\n')
    print(tabulate(amostras, headers=headers))
    print()


def selecionar_amostras():
    sql = 'select * from amostras'
    amostras = ''
    try:
        amostras = cursor.execute(sql)
        amostras = cursor.fetchall()
    except Exception:
        return 2
    finally:
        sleep(2)
        limpa_terminal()

        if len(amostras) == 0:
            print('Não há amostras para classificação. Insira uma nova amostra!\n')
            return 0
        else:
            imprimir_tabulado(
                amostras, ['ID', 'MP10', 'MP25', 'O3', 'CO', 'NO2', 'SO2'])
            return 1


# Lista de cores para exibição do resultado:
VERDE = '\033[1;32m'
AMARELO = '\033[1;33m'
AZUL = '\033[1;34m'
ROXO = '\033[1;35m'
VERMELHO = '\033[1;31m'
LIMPAR = '\033[m'

# Declaração das variáveis para armazenamento das amostras
mp10 = None
mp25 = None
o3 = None
co = None
no2 = None
so2 = None

qualidade_ar = 0
menu = 0

while True:
    interface.menu(['Inserir Amostra', 'Alterar Amostra',
                    'Apagar Amostra', 'Classificar Amostras', 'Sair'])
    try:
        menu = int(input('Qual sua opção? '))
        if menu > 5 or menu <= 0:
            print('\033[31mERRO! Selecione uma opção disponível 1 a 5.\033[m')
            continue
    except:
        print('\033[31mOpção Inválida!\033[m')
        continue

    # Cadastrar uma nova amostra
    if menu == 1:
        print('\nEntre com a leitura dos valores de parâmetros:')
        while True:
            try:
                if mp10 is None:
                    mp10 = float(
                        input('Digite a medida de partículas inaláveis [MP10]: '))
                if mp25 is None:
                    mp25 = float(
                        input('Digite a medida de partículas inaláveis finas [MP25]: '))
                if o3 is None:
                    o3 = float(
                        input('Digite a medida de ozônio [03]:'))
                if co is None:
                    co = float(
                        input('Digite a medida de monóxido de Carbono [CO]: '))
                if no2 is None:
                    no2 = float(
                        input('Digite a medida de dióxido de Nitrogênio [NO2]: '))
                if so2 is None:
                    so2 = float(
                        input('Digite a medida de dióxido de Enxofre [SO2]: '))
                else:
                    break
            except:
                print('Digite apenas números.')

        sql = f'insert into amostras (mp10, mp25, o3, co, no2, so2) values ({mp10}, {mp25}, {o3}, {co}, {no2}, {so2});'

        try:
            cursor.execute(sql)
            conexao.commit()
        except Exception as err:
            print(f'{VERMELHO}Erro ao cadastrar amostra, tente novamente!{LIMPAR}')
        finally:
            limpa_amostras()

            interface.progress()

            print(f'\n{VERDE}SUCESSO!{LIMPAR} Sua amostra foi cadastrada.\n')

            input('\n\nPressione qualquer tecla para continuar...')
            limpa_terminal()

            continue

    # Editar valores de amostras
    elif menu == 2:
        update = selecionar_amostras()

        if update == 1:
            ...
        elif update == 2:
            print(f'{VERMELHO}Erro ao selecionar amostras, tente novamente!{LIMPAR}')
        # update amostras set {parametro} = {novo_valor} where id = {linha};
        # parametro = input(int('Qual parâmetro você deseja alterar?'))
        # id = 0

    # Deletar uma amostra
    elif menu == 3:
        delete = selecionar_amostras()

        # conexao.commit()

    # Classificar amostras
    elif menu == 4:
        try:
            amostras = cursor.execute(
                'select avg(mp10), avg(mp25), avg(o3), avg(co), avg(no2), avg(so2) from amostras;')
            amostras = cursor.fetchall()
        except Exception as err:
            print(f'{VERMELHO}Erro ao selecionar amostras, tente novamente!{LIMPAR}')
        finally:

            if amostras is None:
                print('Não há amostras para classificação. Insira uma nova amostra!\n')
            else:
                for a in amostras:
                    mp10 = a[0]
                    mp25 = a[1]
                    o3 = a[2]
                    co = a[3]
                    no2 = a[4]
                    so2 = a[5]

                # Verificar qualidade para MP10:
                if mp10 >= 0:
                    if mp10 > 250:
                        qualidade_ar = 5
                    elif mp10 > 150:
                        qualidade_ar = 4
                    elif mp10 > 100:
                        qualidade_ar = 3
                    elif mp10 > 50:
                        qualidade_ar = 2
                    else:
                        qualidade_ar = 1
                # Verificar qualidade para MP2,5:

                if mp25 >= 0:
                    if mp25 > 125:
                        if qualidade_ar < 5:
                            qualidade_ar = 5
                    elif mp25 > 75:
                        if qualidade_ar < 4:
                            qualidade_ar = 4
                    elif mp25 > 50:
                        if qualidade_ar < 3:
                            qualidade_ar = 3
                    elif mp25 > 50:
                        if qualidade_ar < 2:
                            qualidade_ar = 2

                # Verificar qualidade para O3:
                if o3 >= 0:
                    if o3 > 200:
                        if qualidade_ar < 5:
                            qualidade_ar = 5
                    elif o3 > 160:
                        if qualidade_ar < 4:
                            qualidade_ar = 4
                    elif o3 > 130:
                        if qualidade_ar < 3:
                            qualidade_ar = 3
                    elif o3 > 100:
                        if qualidade_ar < 2:
                            qualidade_ar = 2

                # Verificar qualidade para CO:
                if co >= 0:
                    if co > 15:
                        if qualidade_ar < 5:
                            qualidade_ar = 5
                    elif co > 13:
                        if qualidade_ar < 4:
                            qualidade_ar = 4
                    elif co > 11:
                        if qualidade_ar < 3:
                            qualidade_ar = 3
                    elif co > 9:
                        if qualidade_ar < 2:
                            qualidade_ar = 2

                # Verificar qualidade para NO2:
                if no2 >= 0:
                    if no2 > 1130:
                        if qualidade_ar < 5:
                            qualidade_ar = 5
                    elif no2 > 320:
                        if qualidade_ar < 4:
                            qualidade_ar = 4
                    elif no2 > 240:
                        if qualidade_ar < 3:
                            qualidade_ar = 3
                    elif no2 > 200:
                        if qualidade_ar < 2:
                            qualidade_ar = 2

                # Verificar qualidade para SO2:
                if so2 >= 0:
                    if so2 > 800:
                        if qualidade_ar < 5:
                            qualidade_ar = 5
                    elif so2 > 365:
                        if qualidade_ar < 4:
                            qualidade_ar = 4
                    elif so2 > 40:
                        if qualidade_ar < 3:
                            qualidade_ar = 3
                    elif so2 > 20:
                        if qualidade_ar < 2:
                            qualidade_ar = 2
                print('\n')
                if qualidade_ar == 5:
                    print(
                        f'A qualidade do ar está: {VERMELHO}PÉSSIMA{LIMPAR}!')
                    print('Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupo sensíveis.')
                elif qualidade_ar == 4:
                    print(
                        f'A qualidade do ar está: {ROXO}MUITO RUIM{LIMPAR}!')
                    print('Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).')
                elif qualidade_ar == 3:
                    print(f'A qualidade do ar está: {AZUL}RUIM{LIMPAR}!')
                    print('Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos, e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.')
                elif qualidade_ar == 2:
                    print(
                        f'A qualidade do ar está: {AMARELO}MODERADA{LIMPAR}!')
                    print('Pessoas de grupos sensíveis (crianças, idosos, e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.')
                elif qualidade_ar == 1:
                    print(f'A qualidade do ar está: {VERDE}BOA{LIMPAR}!')
                else:
                    print(
                        'Não foi possível, realizar a classificação, tente novamente.')

                print(interface.line())

                input('\n\nPressione qualquer tecla para continuar...')
                limpa_terminal()

    elif menu == 5:
        print('Saindo...')
        break

cursor.close()
conexao.close()
