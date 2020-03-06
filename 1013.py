#Exercício 1013 do URI. Receber 3 inteiros e exibir na tela qual deles é o maior

import math

linha1 = input().split(" ")

a,b,c = linha1

a = int(a)
b = int(b)
c = int(c)

maiorAB = int((a+b+math.fabs(a-b))/2)

if c > maiorAB:
    print('{} eh o maior'.format(c))
else:
    print('{} eh o maior'.format(maiorAB))
