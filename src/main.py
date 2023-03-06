print('Entre com a leitura dos valores de parâmetros:')

particulasInalaveis = input('Partículas inaláveis (24h)')
particulasInalaveisFinas = input('Partículas inaláveis finas (24h)')
ozonio = input('Partículas inaláveis finas (8h)')
monoxidoCarbono = input('Partículas inaláveis finas (8h)')
dioxidoNitrogenio = input('Partículas inaláveis finas (8h)')
dioxidoEnxofre = input('Partículas inaláveis finas (8h)')

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

# Verificar qualidade para CO:

# Verificar qualidade para NO2:

# Verificar qualidade para SO2:
