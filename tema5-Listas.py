'''
  una lista es una secuencia de elementos
[]
'''
lista1=["Mario",22,29.5,True,"German",20,9]

print(lista1)
print(lista1 [:])
print(lista1[2])
print(lista1[-1])
print(lista1[0:3])
print(lista1[3:])

lista1.append("Vargas")
print(lista1)

lista1.insert("Nadia")
print(lista1)

lista1.extend(["uno",1,1,False])
print(lista1)
lista1.remove(33)
print(lista1)
lista1.pop()
print(lista1)

lista2=["tres","cuatro"]
lista3=lista1+lista2
print(lista3)

print(lista2*4)

lista4=[2,1,5,4,3]
print(lista4)
lista4.sort()
print(lista4)

del lista4[0]
print(lista4)