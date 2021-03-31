# archivo editado para la rama web 

"""
cadena=input("ingresar una cadena: ")
contador=0

for x in range(1,len(cadena)-1):
    if cadena [x-1]==" " and cadena[x]!=" ":
        contador=contador+1
        print(contador)
print("el numero de palabras es:  ", contador+1)
""""
cadena=input("ingresar una cadena: ")
contador=0
anterior= ""#cadena vacia
for caracter in cadena:
    if caracter !=" " and anterior ==" ":
        contador=contador+1
    anterior=caracter
palabras=contador +1
print("el numero de palabras es : ", palabras)
