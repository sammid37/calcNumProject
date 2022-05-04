import matplotlib.pyplot as plt
from numpy import log as ln

import json

# ------------------------------------- ETAPA 0 (armazenando em listas)
def armazenar_em_lista(data_list):
    # Armazena as alturas, peso, idades e nomes de todos os jogadores
    lista_alturas = [] #0
    lista_pesos = [] #1
    lista_idades = [] #2
    lista_nomes = [] #3

    for i in data_list:
        for key, value in i.items():
            if key == 'ALTURA':
                lista_alturas.append(value)
            elif key == 'PESO':
                lista_pesos.append(value)
            elif key == 'IDADE':
                lista_idades.append(value)
            elif key == 'NOME':
                lista_nomes.append(value)
    return lista_alturas, lista_pesos, lista_idades, lista_nomes

# ------------------------------------- ETAPA 1 (Cálculo de IMCs e valores médios)
def calc_imc(m, h):
    imc = m / h**2

    # até 4 casas decimais
    imc = round(imc, 4)

    return imc

def calc_imc_medio(lista_imcs):
    y = sum(lista_imcs) / len(lista_imcs)
    return y

def delta_imc_medio(y):
    delta_y = abs(25 - y) / y
    return delta_y

def imc_aceitavel(delta_y, y):
    # onde y corresponde ao valor obtido na função imc_medio
    k0 = (1-delta_y)*y 
    k1 = (1+delta_y)*y

    # verifica se o imc está entre o intervalo: k0 <= y <= k1
    if(k0 <= y and y <= k1):
        print("IMC aceitável")
        return y
    else:
        print("Fora do intervalo")
        return 0

def calcular_altura_media(lista_alturas):
    h = sum(lista_alturas) / len(lista_alturas)
    return h

def calc_h_min_h_max():
    pass

# ------------------------------------- ETAPA 2 (Cálculo da Taxa Metabólica Basal)
def calc_tmb(idade, m, h):
    # equação proveniente do 'artigo 1' enviado pelo professor
    tmb = -0.1631 - 0.00255 * idade + 0.4721 * ln(m) + 0.2952 * ln(h)
    return tmb

posicao = ""
while(posicao != "ATACANTE" or posicao != "DEFENSOR" or posicao != "MEIO-CAMPO"):
    posicao = input("Informe a posicação do jogador(ATACANTE, DEFENSOR ou MEIO-CAMPO):")
    if (posicao == "ATACANTE" or posicao == "DEFENSOR" or posicao == "MEIO-CAMPO"):
        print("Posição de campo válida.")
        break
    else:
        print("Posição de campo inválida, tente novamente.")

# Abre o arquivo .json referente a posição do jogador
if (posicao == "ATACANTE"):
    print("Vamos montar o time perfeito de atacantes.")
    f  = open("json/atacantes.json")
    data_list = json.load(f)
elif (posicao == "DEFENSOR"):
    print("Vamos montar o time perfeito de defensores.")
    f = open("json/defensores.json")
    data_list = json.load(f)
else:
    print("Vamos montar o time perfeito de meio-campistas.")
    f = open("json/meiocampos.json")
    data_list = json.load(f)

# Abrindo o arquivo .json referente a posição de Goleiro
f_goleiro = open("json/goleiros.json")
data_list_goleiros = json.load(f_goleiro)

# Armazena em uma lista todos os atributos dos jogadores
# listas = [[], [], [], []]
listas = armazenar_em_lista(data_list)
lista_alturas = listas[0]
lista_pesos = listas[1]
lista_idades = listas[2]
lista_nomes = listas[3]

listas_goleiros = armazenar_em_lista(data_list_goleiros)
lista_alturas_g = listas_goleiros[0]
lista_pesos_g = listas_goleiros[1]
lista_idades_g = listas_goleiros[2]
lista_nomes_g = listas_goleiros[3]

# Para armazenar os dados dos jogadores
# nome_e_dados = [nome, [m,h,i,imc]]
time = []

# ------------------- 1
# Referente a uma das posições informadas pelo usuário: ATACANTE, DEFENSOR e MEIO-CAMPO
imcs = []
for i in range(len(data_list)):
    # 0 0 
    imc_atual = calc_imc(lista_pesos[i], lista_alturas[i])
    nomes_e_dados = [lista_nomes[i], []] 
    nomes_e_dados[1].append(lista_alturas[i])
    nomes_e_dados[1].append(lista_pesos[i])
    nomes_e_dados[1].append(lista_idades[i])
    nomes_e_dados[1].append(imc_atual)

    imcs.append(imc_atual)
    time.append(nomes_e_dados)
print(f"Foram armazenados os dados de {len(time)} de jogadores.")

# Referente a posição de GOLEIRO
# ****** É necessário realizar os mesmo procedimentos para os goleiros!

print(f"Foram calculados {len(imcs)} IMCs referente aos jogadores que atuam como {posicao}")

# Calculo do imc_medio (y)
y = calc_imc_medio(imcs) 
print(f"O IMC médio dos jogadores que atuam como {posicao} é de {y:.4f}.")
# Variação de IMC's
delta_y = delta_imc_medio(y)
print(f"O valor da variação de IMCs é de {delta_y}")

# CHAMAR a função que calcula imc aceitável
# CHAMAR a função que calcula altura média

# Critério para escolher o jogador
# Calcular esse intervalo [h0, h1] e apontar qual jogador tá dentro desse intervalo
# CHAMAR a função que calcula h0 h1
# Possa ser que necessite chamar a matriz (abaixo) 

# Para a montagem do time perfeito
# se a altura H estiver dentro do intervalo [h0,h1]
# time_perfeito.append(nome_e_dados[indice])
time_perfeito = []

# lendo a matriz
# for linha in time:
   
# ------------------- 2
# Método da Bisseção ou Newton 