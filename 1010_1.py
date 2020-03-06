#Exercício 1010 do URI. Receber dois produtos diferentes, seus códigos, quantidades e preços unitários.
#Calcular e exibir o total a pagar

linha1 = input().split(" ")
linha2 = input().split(" ")

codProd1,qtdeProd1,precoProd1 = linha1
codProd2, qtdeProd2, precoProd2 = linha2

produto1 = [int(codProd1), int(qtdeProd1), float(precoProd1)]
produto2 = [int(codProd2), int(qtdeProd2), float(precoProd2)]

totalProd1 = float(produto1[1]*produto1[2])
totalProd2 = float(produto2[1]*produto2[2])

print('VALOR A PAGAR: R$ {0:.2f}'.format(totalProd1+totalProd2))