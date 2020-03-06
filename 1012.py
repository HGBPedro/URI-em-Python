#Exercicio 1012 do URI. Receber 3 números de ponto flutuante, calcular e exibir o resultado da área
#do triângulo(b*h/2), círculo(pi*r²), trapézio(((b1+b2)*2)/2), quadrado(b²) e retângulo(b*h)

import math

linha1 = input().split(" ")

a,b,c = linha1
a = float(a)
b = float(b)
c = float(c)

print('TRIANGULO: {0:.3f}'.format((a*c)/2))
print('CIRCULO: {0:.3f}'.format(3.14159*math.pow(c,2)))
print('TRAPEZIO: {0:.3f}'.format(((a+b)*c)/2))
print('QUADRADO: {0:.3f}'.format(math.pow(b,2)))
print('RETANGULO: {0:.3f}'.format(a*b))