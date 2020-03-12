sec = float(input())
min = 0
hora = 0

while sec > 60:
    min = min + 1
    sec = sec - 60
    if min > 60:
        hora = hora +1
        min =  min - 60
#hora = (sec/60)/60
#min = hora * 60

print('{}:{}:{}'.format(int(hora),int(min),int(sec)))        