#Problema 1009 do URI. Salário com bonus. Recebe o nome do funcionário,
#o salário fixo e o total de vendas no mês. Exibir o salário total somando
#ao salário fixo uma comissão de 15% em cima do total de vendas

nome = input()
salFixo = float(input())
vendas = float(input())

comissao = vendas * 0.15
salTotal = salFixo + comissao

print('TOTAL = R$ {0:.2f}'.format(salTotal))
