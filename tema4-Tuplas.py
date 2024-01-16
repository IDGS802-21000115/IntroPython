'''
Las tuplas son como arreglos, solo que no se pueden modificar una vez que las creamos
()
'''
tupla=("uno","dos","tres")
print(tupla)
print(type(tupla))

tuplaVariosDatos=(12,True,23.6,"Nombre",12+3j)
print(tuplaVariosDatos)

tuplasConTuplas=(1,2,3,4,(1,2,3))
print(tuplasConTuplas)

'''
Para recorrer las tuplas
'''
print(tuplaVariosDatos[3])
print(tuplaVariosDatos[-2])
print(tuplaVariosDatos[0.2])


a,b,c=tupla
print(a)
print(b)
print(c)