import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Equação: y' = y - t^2 + 1

""" Solução por Método de Euler """

a = 0 # Início do intervalo eixo (t)
b = 2 # Fim do intervalo eixo (t)
N = 10  # Quantidade de pontos eixo (t)
t = np.linspace(a,b, N) # Cria um vetor de 10 pontos entre o intervalo [a,b]

h = (b-a)/N # Calcula o espaçamento necessário para cada ponto
w = np.zeros(N) # Inicializa omega com um vetor de zeros
w[0] = 0.5 # Valor inicial dado no enunciado

for i in range(0, N-1):
    w[i+1] = w[i] + h * (w[i] - pow(t[i],2) + 1)


""" Solução analítica """
# Resolvida: y(t) = (t + 1)^2 + C*e^t
# Assumindo y0 = 0,5, temos: y(t) = (t +1)^2 - 0,5e^t

solAnalitica = pow((t + 1),2) - 0.5*np.exp(t)

erro = np.abs(solAnalitica - w) # Cálculo da diferença entre as soluções

""" Tabela de pontos (console)"""
dados = {
    "Tempo (t_i)": t,
    "Aproximação de Euler (w_i)": w,
    "Solução Analítica (y_i) ": solAnalitica,
    "Erro Absoluto |y_i - w_i|": erro
}
arqExcel = "resultados.xlsx"
DFResultado = pd.DataFrame(dados) # Cria um DataFrame (tabela)
DFResultado.to_excel(arqExcel, index=False)
print(f"Dados salvos com sucesso no arquivo: {arqExcel}")


""" Plotagem dos gráficos """
plt.figure(figsize=(10, 6))
plt.plot(t, solAnalitica, 'r-o', label="Solução Analitica")
plt.plot(t, w, 'b--x', label="Solução pelo Método de Euler")
plt.title("Comparação: Método de Euler vs. Solução Analítica")
plt.xlabel("Tempo (t)")
plt.ylabel("y(t)")
plt.grid(True)
plt.legend()
plt.show()


