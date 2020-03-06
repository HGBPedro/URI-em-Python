#Exercício 1010 do URI. Receber dois produtos diferentes, seus códigos, quantidades e preços unitários.
#Calcular e exibir o total a pagar

linha1 = input().split(" ")
linha2 = input().split(" ")

codProd1,qtdeProd1,precoProd1 = linha1
codProd2, qtdeProd2, precoProd2 = linha2

codProd1 = int(codProd1)
qtdeProd1 = int(qtdeProd1)
precoProd1 = float(precoProd1)
codProd2 = int(codProd2)
qtdeProd2 = int(qtdeProd2)
precoProd2 = float(precoProd2)

total = (qtdeProd1*precoProd1)+(qtdeProd2*precoProd2)


print('VALOR A PAGAR: R$ {0:.2f}'.format(total))
