print("suma de Numeros")

num1=int(input("dame el valor de n1"))
num2=int(input("dame el valor de n2"))

if num1 > num2 :
    print("EL {} es mayor que el {}".format(num1,num2)) 
else :
     print("EL {} es mayor que el {}".format(num2,num1)) 


print("---------------------------pedir una edad---------------------------------------")

edad=int(input("Ingrese su edad"))
if edad >18:
    print(" Eres mayor de edad")
elif edad ==18:
    print("tienes 18")
else:
    print("No eres mayor de edad")