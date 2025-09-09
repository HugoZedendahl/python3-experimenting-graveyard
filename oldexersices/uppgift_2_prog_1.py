minLista = ["Stocholm","London","Beijing","New York","Vällinge"]

minLista.append("Paris")

print(minLista)

minMedelLista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for x in minMedelLista:
    print(x*2)

minMedelLista.remove(1)
#tar bort värdet 1
print(minMedelLista)

minMedelLista.pop(1)
#tar bort det andra värdet i indexet
print(minMedelLista)

minAdvLista = ["ett",2,"tre",4,True]

minAdvStrLista = [x for x in minAdvLista if isinstance(x, str) ]
#tar bort alla värden som inte är en string
print(minAdvStrLista)

minJäm1Lista = [1,3,5,7,9]
#udda nummer
minJäm2Lista =[2,3,5,7,11]
#primtal
minAggLista = [x for x in minJäm1Lista if x in minJäm2Lista]
#udda numer som är primtal
print(minAggLista)

listLista = [1,2,3,4,5]

minTuple = (1,2,3,4,5)

mittSet = {1,2,3,4,5}

try:
    listLista.pop(2)
except:
    print("kunde inte .pop()")

print(listLista)

try:
    minTuple.pop(2)
except:
    print("kunde inte .pop() på "+str(type(minTuple)))

print(minTuple)

try:
    mittSet.pop(2)
except:
    print("kunde inte .pop() på "+str(type(mittSet)))

print(mittSet)

#du kan göra .pop på en lista, men ej på en tuple då den är icke mutabel, och ett set har inte ett index att referera till för att använda .pop()