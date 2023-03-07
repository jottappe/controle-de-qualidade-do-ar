print('Entre com a leitura dos valores de parâmetros:')

particulasInalaveis = int(input('Partículas inaláveis (24h) '))
particulasInalaveisFinas = int(input('Partículas inaláveis finas (24h) '))
ozonio = int(input('Ozônio (8h) '))
monoxidoCarbono = int(input('Monóxido de Carbono (8h) '))
dioxidoNitrogenio = int(input('Dióxido de Nitrogênio (8h) '))
dioxidoEnxofre = int(input('Dióxido de Enxofre (8h) '))

qualidadeMP10 = 0
qualidadeMP25 = 0
qualidadeOzonio = 0
qualidadeMonoxidoCarbono = 0
qualidadeDioxidoNitrogenio = 0
qualidadeDioxidoEnxofre = 0

# Lista de cores para exibição do resultado:
BOA = '\033[1;32m'
MODERADA = '\033[1;33m'
RUIM = '\033[1;34m'
MUITORUIM = '\033[1;35m'
PESSIMA = '\033[1;31m'
LIMPAR = '\033[m'

# Verificar qualidade para MP10:
if particulasInalaveis > 0 and particulasInalaveis <= 50:
    qualidadeMP10 = 1
elif particulasInalaveis > 50 and particulasInalaveis <= 100:
    qualidadeMP10 = 2
elif particulasInalaveis > 100 and particulasInalaveis <= 150:
    qualidadeMP10 = 3
elif particulasInalaveis > 150 and particulasInalaveis <= 250:
    qualidadeMP10 = 4
else:
    qualidadeMP10 = 5

# Verificar qualidade para MP2,5:
if particulasInalaveisFinas > 0 and particulasInalaveisFinas <= 25:
    qualidadeMP25 = 1
elif particulasInalaveisFinas > 25 and particulasInalaveisFinas <= 50:
    qualidadeMP25 = 2
elif particulasInalaveisFinas > 50 and particulasInalaveisFinas <= 75:
    qualidadeMP25 = 3
elif particulasInalaveisFinas > 75 and particulasInalaveisFinas <= 125:
    qualidadeMP25 = 4
else:
    qualidadeMP25 = 5

# Verificar qualidade para O3:
if ozonio > 0 and ozonio <= 100:
    qualidadeOzonio = 1
elif ozonio > 100 and ozonio <= 130:
    qualidadeOzonio = 2
elif ozonio > 130 and ozonio <= 160:
    qualidadeOzonio = 3
elif ozonio > 160 and ozonio <= 200:
    qualidadeOzonio = 4
else:
    qualidadeOzonio = 5

# Verificar qualidade para CO:
if monoxidoCarbono > 0 and monoxidoCarbono <= 9:
    qualidadeMonoxidoCarbono = 1
elif monoxidoCarbono > 9 and monoxidoCarbono <= 11:
    qualidadeMonoxidoCarbono = 2
elif monoxidoCarbono > 11 and monoxidoCarbono <= 13:
    qualidadeMonoxidoCarbono = 3
elif monoxidoCarbono > 13 and monoxidoCarbono <= 15:
    qualidadeMonoxidoCarbono = 4
else:
    qualidadeMonoxidoCarbono = 5

# Verificar qualidade para NO2:
if dioxidoNitrogenio > 0 and dioxidoNitrogenio <= 200:
    qualidadeDioxidoNitrogenio = 1
elif dioxidoNitrogenio > 200 and dioxidoNitrogenio <= 240:
    qualidadeDioxidoNitrogenio = 2
elif dioxidoNitrogenio > 240 and dioxidoNitrogenio <= 320:
    qualidadeDioxidoNitrogenio = 3
elif dioxidoNitrogenio > 320 and dioxidoNitrogenio <= 1130:
    qualidadeDioxidoNitrogenio = 4
else:
    qualidadeDioxidoNitrogenio = 5

# Verificar qualidade para SO2:
if dioxidoEnxofre > 0 and dioxidoEnxofre <= 20:
    qualidadeDioxidoEnxofre = 1
elif dioxidoEnxofre > 20 and dioxidoEnxofre <= 40:
    qualidadeDioxidoEnxofre = 2
elif dioxidoEnxofre > 40 and dioxidoEnxofre <= 365:
    qualidadeDioxidoEnxofre = 3
elif dioxidoEnxofre > 365 and dioxidoEnxofre <= 800:
    qualidadeDioxidoEnxofre = 4
else:
    qualidadeDioxidoEnxofre = 5

print(40 * '-')

if qualidadeMP10 == 5 or qualidadeMP25 == 5 or qualidadeOzonio == 5 or qualidadeMonoxidoCarbono == 5 or qualidadeDioxidoNitrogenio == 5 or qualidadeDioxidoEnxofre == 5:
    print(f'A qualidade do ar está: {PESSIMA}PÉSSIMA{LIMPAR}!')
    print('Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupo sensíveis.')
elif qualidadeMP10 == 4 or qualidadeMP25 == 4 or qualidadeOzonio == 4 or qualidadeMonoxidoCarbono == 4 or qualidadeDioxidoNitrogenio == 4 or qualidadeDioxidoEnxofre == 4:
    print(f'A qualidade do ar está: {MUITORUIM}MUITO RUIM{LIMPAR}!')
    print('Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).')
elif qualidadeMP10 == 3 or qualidadeMP25 == 3 or qualidadeOzonio == 3 or qualidadeMonoxidoCarbono == 3 or qualidadeDioxidoNitrogenio == 3 or qualidadeDioxidoEnxofre == 3:
    print(f'A qualidade do ar está: {RUIM}RUIM{LIMPAR}!')
    print('Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos, e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.')
elif qualidadeMP10 == 2 or qualidadeMP25 == 2 or qualidadeOzonio == 2 or qualidadeMonoxidoCarbono == 5 or qualidadeDioxidoNitrogenio == 2 or qualidadeDioxidoEnxofre == 2:
    print(f'A qualidade do ar está: {MODERADA}MODERADA{LIMPAR}!')
    print('Pessoas de grupos sensíveis (crianças, idosos, e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.')
else:
    print(f'A qualidade do ar está: {BOA}BOA{LIMPAR}!')

print(40 * '-')
