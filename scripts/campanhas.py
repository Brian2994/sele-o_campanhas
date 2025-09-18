import pandas as pd
from config import input_path

dados = pd.read_excel(input_path)
print(dados.head())

# Padroniza as colunas para evitar problemas com maiúsculas/minúsculas
dados["Marca"] = dados["Marca"].str.upper()
dados["Canal"] = dados["Canal"].str.upper()
dados["Grupo"] = dados["Grupo"].str.upper()

# === Passo 1: Selecionar Marca ===
listar_marca = dados["Marca"].unique().tolist()
print("\n Marcas disponíveis:")
for m in listar_marca:
    print(f" * {m}") # Mostra a lista

marca_escolhida = input("\nDigite a Marca: ").strip().upper()

# Filtra canais válidos para marca
canais_disponiveis = dados[dados["Marca"] == marca_escolhida]["Canal"].unique().tolist()

# Verifica se a lista canais_disponiveis está vazia.
if not canais_disponiveis:
    print(" Marca inválida ou não encontrada.")
    exit() # Fecha a execução se for verdadeira

# === Passo 2: Selecionar Canal ===
print("\n Canais disponíveis para essa marca:")
for c in canais_disponiveis:
    print(f" * {c}") # Mostra a lista

canal_escolhido = input("\nDigite o Canal: ").strip().upper()

# Filtra grupos válidos para marca + canal
grupos_disponiveis = dados[
    (dados["Marca"] == marca_escolhida) &
    (dados["Canal"] == canal_escolhido)
]["Grupo"].dropna().unique().tolist()

# Verifica se a lista grupos_disponiveis está vazia.
if not grupos_disponiveis:
    print(" Canal inválido ou não encontrado.")
    exit() # Fecha a execução se for verdadeira

# === Passo 3: Selecionar Grupo ===
print("\n Grupos disponíveis para essa combinação:")
for g in grupos_disponiveis:
    print(f" * {g}")

grupo_escolhido = input("\nDigite o Grupo: ").strip().upper()

# === Passo 4: Mostrar resultado ===
filtro_final = dados[
    (dados["Marca"] == marca_escolhida) &
    (dados["Canal"] == canal_escolhido) &
    (dados["Grupo"] == grupo_escolhido)
]

if filtro_final.empty:
    print(" Nenhuma informação encontrada para essa combinação.")
else:
    print("\n Resultado encontrado:")
    print(filtro_final.reset_index(drop=True))
