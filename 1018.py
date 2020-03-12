notas = int(input())

n100 = int(0)
n50 = int(0)
n20 = int(0)
n10 = int(0)
n5 = int(0)
n2 = int(0)
n1 = int(0)

n100 = notas/100
dez = (notas % 100)/10
un = notas % 10

if dez >= 5:
    n50 = 1
    dez = dez - 5
if (dez % 2) != 0:
    n20 = dez / 2
else:
    n10 = 1
    dez = dez-1
    n20 = dez / 2

if un >= 5:
    n5 = 1
    un = un -5
if (un %2) == 0:
    n2 = un / 2
else:
    n1 = 1
    un = un-1
    n2 = un/2

print(notas)
print('{} nota(s) de R$ 100,00'.format(int(n100)))
print('{} nota(s) de R$ 50,00'.format(int(n50)))
print('{} nota(s) de R$ 20,00'.format(int(n20)))
print('{} nota(s) de R$ 10,00'.format(int(n10)))
print('{} nota(s) de R$ 5,00'.format(int(n5)))
print('{} nota(s) de R$ 2,00'.format(int(n2)))
print('{} nota(s) de R$ 1,00'.format(int(n1)))