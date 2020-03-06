#Exercício 1014 do URI. Calcular e exibir o consumo de combustível de um veículo recebendo a quantidade
#de KMs rodados e a quantitade de combustível consumido

kms = int(input())
cons = float(input())

print('{0:.3f} km/l'.format(kms/cons))