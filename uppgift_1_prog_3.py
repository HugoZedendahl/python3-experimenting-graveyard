lista = [1,1,2,3,4,4]

ersätt ={1:5}

lista = [ersätt.get(x,x) for x in lista]

print(lista)