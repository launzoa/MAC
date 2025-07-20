import numpy as np
import pandas as pd

# --- Configuração Inicial ---
x = 1.8
valor_analitico = 1 / x

# --- Listas para armazenar os resultados ---
lista_h = []
lista_dB, lista_dC, lista_dF = [], [], []
lista_erroDB, lista_erroDC, lista_erroDF = [], [], []

# --- Loop para calcular os valores ---

for i in range(1, 9):
    h = 10.0 ** (-i)  # Pega o valor de h para a iteração atual
    lista_h.append(h)

    # Calcula as aproximações para o h atual
    aprox_atrasada = (np.log(x) - np.log(x - h)) / h
    aprox_centrada = (np.log(x + h) - np.log(x - h)) / (2 * h)
    aprox_avancada = (np.log(x + h) - np.log(x)) / h

    # Adiciona os resultados às listas
    lista_dB.append(aprox_atrasada)
    lista_dC.append(aprox_centrada)
    lista_dF.append(aprox_avancada)

    # Adiciona os erros às listas
    lista_erroDB.append(np.abs(valor_analitico - aprox_atrasada))
    lista_erroDC.append(np.abs(valor_analitico - aprox_centrada))
    lista_erroDF.append(np.abs(valor_analitico - aprox_avancada))

# Excel
dados = {
    "h": lista_h,
    "Diferença Atrasada": lista_dB,
    "Erro (Atrasada)": lista_erroDB,
    "Diferença Centrada": lista_dC,
    "Erro (Centrada)": lista_erroDC,
    "Diferença Avançada": lista_dF,
    "Erro (Avançada)": lista_erroDF
}
resultados_df = pd.DataFrame(dados)

nome_arquivo = "resultados1.xlsx"
resultados_df.to_excel(nome_arquivo, index=False, float_format="%.15f")

print("\nDataFrame:")
print(resultados_df)