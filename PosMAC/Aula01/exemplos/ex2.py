import numpy as np
import pandas as pd
import os

x = np.pi / 6; solucao = -5
f = lambda x: 10*np.cos(x)
h = lambda x: 0.1 / 2**x
E = lambda x, y: np.abs(x-y)/x

lista_h = []; lista_dB = []; lista_dC = []; lista_dF = []; lista_EdB = []; lista_EdC = []; lista_EdF = []

for i in range(0,13):
    h_i = h(i)

    dB = (f(x) - f(x-h_i)) / h_i
    dC = (f(x+h_i) - f(x-h_i)) / (2*h_i)
    dF = (f(x+h_i) - f(x)) / h_i

    EdB = E(solucao, dB)
    EdC = E(solucao, dC)
    EdF = E(solucao, dF)

    lista_h.append(h_i)
    lista_dB.append(dB)
    lista_dC.append(dC)
    lista_dF.append(dF)
    lista_EdB.append(EdB)
    lista_EdC.append(EdC)
    lista_EdF.append(EdF)

dados = {
    'h': lista_h,
    'dB': lista_dB,
    'dC': lista_dC,
    'dF': lista_dF,
    'EdB': lista_EdB,
    'EdC': lista_EdC,
    'EdF': lista_EdF
}
resultadosDF = pd.DataFrame(data=dados)
arqExcel = "resultados2.xlsx"
resultadosDF.to_excel(arqExcel, index=False, float_format='%.15f')

os.startfile(arqExcel)