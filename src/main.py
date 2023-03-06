print('Entre com a leitura dos valores de parâmetros:')

particulasInalaveis = input('Partículas inaláveis (24h)')
particulasInalaveisFinas = input('Partículas inaláveis finas (24h)')
ozonio = input('Ozônio (8h)')
monoxidoCarbono = input('Monóxido de Carbono (8h)')
dioxidoNitrogenio = input('Dióxido de Nitrogênio (8h)')
dioxidoEnxofre = input('Dióxido de Enxofre (8h)')

qualidadeMP10 = 0
qualidadeMP25 = 0
qualidadeOzonio = 0
qualidadeMonoxidoCarbono = 0
qualidadeDioxidoNitrogenio = 0
qualidadeDioxidoEnxofre = 0

# Verificar qualidade para MP10:
if particulasInalaveis > 0 and particulasInalaveis <= 50:
    qualidadeMP10 = 1
elif particulasInalaveis > 50 and particulasInalaveis <= 100:
    qualidadeMP10 = 2
elif particulasInalaveis > 100 and particulasInalaveis <= 150:
    qualidadeMP10 = 3
elif particulasInalaveis > 100 and particulasInalaveis <= 250:
    qualidadeMP10 = 4
else:
    qualidadeMP10 = 5

# Verificar qualidade para MP2,5:
if particulasInalaveis > 0 and particulasInalaveis <= 25:
    qualidadeMP25 = 1
elif particulasInalaveis > 25 and particulasInalaveis <= 50:
    qualidadeMP25 = 2
elif particulasInalaveis > 50 and particulasInalaveis <= 75:
    qualidadeMP25 = 3
elif particulasInalaveis > 75 and particulasInalaveis <= 125:
    qualidadeMP25 = 4
else:
    qualidadeMP25 = 5

# Verificar qualidade para O3:
if particulasInalaveis > 0 and particulasInalaveis <= 100:
    qualidadeOzonio = 1
elif particulasInalaveis > 100 and particulasInalaveis <= 130:
    qualidadeOzonio = 2
elif particulasInalaveis > 130 and particulasInalaveis <= 160:
    qualidadeOzonio = 3
elif particulasInalaveis > 160 and particulasInalaveis <= 200:
    qualidadeOzonio = 4
else:
    qualidadeOzonio = 5

# Verificar qualidade para CO:
if particulasInalaveis > 0 and particulasInalaveis <= 9:
    qualidadeMonoxidoCarbono = 1
elif particulasInalaveis > 9 and particulasInalaveis <= 11:
    qualidadeMonoxidoCarbono = 2
elif particulasInalaveis > 11 and particulasInalaveis <= 13:
    qualidadeMonoxidoCarbono = 3
elif particulasInalaveis > 13 and particulasInalaveis <= 15:
    qualidadeMonoxidoCarbono = 4
else:
    qualidadeMonoxidoCarbono = 5

# Verificar qualidade para NO2:
if particulasInalaveis > 0 and particulasInalaveis <= 200:
    qualidadeDioxidoNitrogenio = 1
elif particulasInalaveis > 200 and particulasInalaveis <= 240:
    qualidadeDioxidoNitrogenio = 2
elif particulasInalaveis > 240 and particulasInalaveis <= 320:
    qualidadeDioxidoNitrogenio = 3
elif particulasInalaveis > 320 and particulasInalaveis <= 1130:
    qualidadeDioxidoNitrogenio = 4
else:
    qualidadeDioxidoNitrogenio = 5

# Verificar qualidade para SO2:
if particulasInalaveis > 0 and particulasInalaveis <= 20:
    qualidadeDioxidoEnxofre = 1
elif particulasInalaveis > 20 and particulasInalaveis <= 40:
    qualidadeDioxidoEnxofre = 2
elif particulasInalaveis > 40 and particulasInalaveis <= 365:
    qualidadeDioxidoEnxofre = 3
elif particulasInalaveis > 365 and particulasInalaveis <= 800:
    qualidadeDioxidoEnxofre = 4
else:
    qualidadeDioxidoEnxofre = 5
