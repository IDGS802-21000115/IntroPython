num1=20
num2=4
print("La suma es:",(num1+num2))
print("La esta es:",(num1-num2))
print("La multiplicacion es:",(num1*num2))
print("La division es:",(num1/num2))
print("La division exacta es:",(num1//num2))
print("la potencia es:",(num1**num2))

#Concatenacion en Python

texto1="Hola"
Texto2="Mundo"
textoFinal=texto1+" "+Texto2 
print(textoFinal)
print("El saludo es: %s %s" %(texto1, Texto2))

saludoFinal="Saludo {} {}".format(texto1,Texto2)
print(saludoFinal)

saludoFinal2="Saludo {y} {x}".format(x=texto1,y=Texto2)
print(saludoFinal2)
