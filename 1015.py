#Exercício 1015 do URI. Calcular e exibir a distância de dois pontos recebendo quatro variáveis de ponto flutuante
#e utilizando a formula √(x2-x1)²+(y2-y1)²

import math

linha1 = input().split(" ")
linha2 = input().split(" ")

x1, y1 = linha1
x2, y2 = linha2

x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)

print('{0:.4f}'.format(math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))))