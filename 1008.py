#Problema 1008 do URI, calcular o salario do funcionario a partir das horas trabalhadas
#e o valor da hora. Exibir o numero do funcionario e o salario

number = int(input())
horas = int(input())
valHora = float(input())

salario = float(horas * valHora)

print('NUMBER = {}'.format(number))
print('SALARY = U$ {0:.2f}'.format(salario))
