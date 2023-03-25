print('Entre com a leitura dos valores de parâmetros:\n')

particulas_inalaveis = None
particulas_inalaveis_finas = None
ozonio = None
monoxido_carbono = None
dioxido_nitrogenio = None
dioxido_enxofre = None

qualidade_ar = 0

while True:
    try:
        if particulas_inalaveis == None:
            particulas_inalaveis = float(
                input('Digite a medida de partículas inaláveis (24h) '))
        if particulas_inalaveis_finas == None:
            particulas_inalaveis_finas = float(
                input('Digite a medida de partículas inaláveis finas (24h) '))
        if ozonio == None:
            ozonio = float(input('Digite a medida de ozônio (8h) '))
        if monoxido_carbono == None:
            monoxido_carbono = float(
                input('Digite a medida de monóxido de Carbono (8h) '))
        if dioxido_nitrogenio == None:
            dioxido_nitrogenio = float(
                input('Digite a medida de dióxido de Nitrogênio (8h) '))
        if dioxido_enxofre == None:
            dioxido_enxofre = float(
                input('Digite a medida de dióxido de Enxofre (8h) '))
        else:
            break
    except:
        print('Digite apenas números.')


# Lista de cores para exibição do resultado:
BOA = '\033[1;32m'
MODERADA = '\033[1;33m'
RUIM = '\033[1;34m'
MUITORUIM = '\033[1;35m'
PESSIMA = '\033[1;31m'
LIMPAR = '\033[m'

# Verificar qualidade para MP10:
if particulas_inalaveis >= 0:
    if particulas_inalaveis > 250:
        qualidade_ar = 5
    elif particulas_inalaveis > 150:
        qualidade_ar = 4
    elif particulas_inalaveis > 100:
        qualidade_ar = 3
    elif particulas_inalaveis > 50:
        qualidade_ar = 2
    else:
        qualidade_ar = 1

# Verificar qualidade para MP2,5:
if particulas_inalaveis_finas >= 0:
    if particulas_inalaveis_finas > 125:
        if qualidade_ar < 5:
            qualidade_ar = 5
    elif particulas_inalaveis_finas > 75:
        if qualidade_ar < 4:
            qualidade_ar = 4
    elif particulas_inalaveis_finas > 50:
        if qualidade_ar < 3:
            qualidade_ar = 3
    elif particulas_inalaveis_finas > 50:
        if qualidade_ar < 2:
            qualidade_ar = 2

# Verificar qualidade para O3:
if ozonio >= 0:
    if ozonio > 200:
        if qualidade_ar < 5:
            qualidade_ar = 5
    elif ozonio > 160:
        if qualidade_ar < 4:
            qualidade_ar = 4
    elif ozonio > 130:
        if qualidade_ar < 3:
            qualidade_ar = 3
    elif ozonio > 100:
        if qualidade_ar < 2:
            qualidade_ar = 2

# Verificar qualidade para CO:
if monoxido_carbono >= 0:
    if monoxido_carbono > 15:
        if qualidade_ar < 5:
            qualidade_ar = 5
    elif monoxido_carbono > 13:
        if qualidade_ar < 4:
            qualidade_ar = 4
    elif monoxido_carbono > 11:
        if qualidade_ar < 3:
            qualidade_ar = 3
    elif monoxido_carbono > 9:
        if qualidade_ar < 2:
            qualidade_ar = 2

# Verificar qualidade para NO2:
if dioxido_nitrogenio >= 0:
    if dioxido_nitrogenio > 1130:
        if qualidade_ar < 5:
            qualidade_ar = 5
    elif dioxido_nitrogenio > 320:
        if qualidade_ar < 4:
            qualidade_ar = 4
    elif dioxido_nitrogenio > 240:
        if qualidade_ar < 3:
            qualidade_ar = 3
    elif dioxido_nitrogenio > 200:
        if qualidade_ar < 2:
            qualidade_ar = 2

# Verificar qualidade para SO2:
if dioxido_enxofre >= 0:
    if dioxido_enxofre > 800:
        if qualidade_ar < 5:
            qualidade_ar = 5
    elif dioxido_enxofre > 365:
        if qualidade_ar < 4:
            qualidade_ar = 4
    elif dioxido_enxofre > 40:
        if qualidade_ar < 3:
            qualidade_ar = 3
    elif dioxido_enxofre > 20:
        if qualidade_ar < 2:
            qualidade_ar = 2

print(40 * '-')

if qualidade_ar == 5:
    print(f'A qualidade do ar está: {PESSIMA}PÉSSIMA{LIMPAR}!')
    print('Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupo sensíveis.')
elif qualidade_ar == 4:
    print(f'A qualidade do ar está: {MUITORUIM}MUITO RUIM{LIMPAR}!')
    print('Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).')
elif qualidade_ar == 3:
    print(f'A qualidade do ar está: {RUIM}RUIM{LIMPAR}!')
    print('Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos, e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.')
elif qualidade_ar == 2:
    print(f'A qualidade do ar está: {MODERADA}MODERADA{LIMPAR}!')
    print('Pessoas de grupos sensíveis (crianças, idosos, e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.')
elif qualidade_ar == 1:
    print(f'A qualidade do ar está: {BOA}BOA{LIMPAR}!')
else:
    print('Não foi possível, realizar a classificação, tente novamente.')

print(40 * '-')
