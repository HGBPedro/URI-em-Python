#Exercício 1011 do URI. Receber o raio de uma esfera, calcular seu volume e exibir o resultado

import math

raio = float(input())

vol = (4/3.0) * 3.14159 * math.pow(raio,3)

print('VOLUME = {0:.3f}'.format(vol))
