import numpy as np
import matplotlib.pyplot as plt

# Método de Euler implícito
# # Equação: y' = y - t^2 + 1, com o valor inicial de y(0) = 0.5


a = 0 # Início do intervalo eixo (t)
b = 2 # Fim do intervalo eixo (t)
N = 10  # Quantidade de pontos eixo (t)
h = (b-a)/N # Calcula o espaçamento necessário para cada ponto

w = np.zeros(N) # Inicializa omega com um vetor de zeros
w[0] = 0.5 # Valor inicial dado no enunciado

t = np.arange(a, b, h) # Cria um vetor de 10 pontos entre o intervalo [a,b]

# Solução numérica
for i in range(0, N-1):
    w[i + 1] = (w[i] + h * (1 - t[i + 1]**2)) / (1 - h)

# Solução analítica
# Resolvida: y(t) = (t + 1)^2 + C*e^t
# Assumindo y0 = 0,5, temos: y(t) = (t +1)^2 - 0,5e^t
solAnalitica = pow((t + 1),2) - 0.5*np.exp(t)

# Plotagem
plt.plot(t, solAnalitica, 'r-', label='Solução analítica')
plt.plot(t, w, 'b-', label='Euler implícito')
plt.xlabel('Tempo (t)')
plt.ylabel('y(t)')
plt.legend()
plt.show()