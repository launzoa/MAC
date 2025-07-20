import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

fx = lambda x: np.exp(np.sin(x)) # Função original
dfx_exata = lambda x: np.cos(x) * np.exp(np.sin(x)) # Derivada exata

E_local = lambda exato, aproximado: np.abs(exato - aproximado) # Erro local
E_relativo = lambda exato, aproximado: np.abs(exato - aproximado) / np.abs(exato) # Erro relativo

a = 0.5; b = 1.5
lista_de_dataframes = []


for i in range(0, 3):
    h = 1 / 10**(i+1)

    x_vals = np.arange(a, b, h)

    dfx_vals = dfx_exata(x_vals)
    dB_vals = (fx(x_vals) - fx(x_vals - h)) / h
    dC_vals = (fx(x_vals + h) - fx(x_vals - h)) / (2*h)
    dF_vals = (fx(x_vals + h) - fx(x_vals)) / h

    ELdB_vals = E_local(dfx_vals, dB_vals)
    ELdC_vals = E_local(dfx_vals, dC_vals)
    ELdF_vals = E_local(dfx_vals, dF_vals)

    ERdB_vals = E_relativo(dfx_vals, dB_vals)
    ERdC_vals = E_relativo(dfx_vals, dC_vals)
    ERdF_vals = E_relativo(dfx_vals, dF_vals)

    dados_iteracao = {
        'h': h,
        'x': x_vals,
        'Derivada_Exata': dfx_vals,
        'Derivada_Atrasada': dB_vals,
        'Erro_Local_Atrasada': ELdB_vals,
        'Erro_Relativo_Atrasada': ERdB_vals,
        'Derivada_Centrada': dC_vals,
        'Erro_Local_Centrada': ELdC_vals,
        'Erro_Relativo_Centrada': ERdC_vals,
        'Derivada_Avancada': dF_vals,
        'Erro_Local_Avancada': ELdF_vals,
        'Erro_Relativo_Avancada': ERdF_vals,
    }

    df_iteracao = pd.DataFrame(data=dados_iteracao)
    lista_de_dataframes.append(df_iteracao)

    plt.plot(x_vals, dfx_vals, 'b-', label=f'Solução exata (h={h})')
    plt.plot(x_vals, dB_vals, 'g-', label=f'Diferença Atrasada (h={h})')
    plt.plot(x_vals, dC_vals, 'r-', label=f'Diferença Centrada (h={h})')
    plt.plot(x_vals, dF_vals, 'y-', label=f'Diferença Avançada (h={h})')

    plt.title("Comparação entre Derivada Exata e Métodos Numéricos")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    plt.show()

resultadosDF = pd.concat(lista_de_dataframes, ignore_index=True)
arqExcel = "resultados_ex4.xlsx"
resultadosDF.to_excel(arqExcel, index=False, float_format='%.15f')

os.startfile(arqExcel)
