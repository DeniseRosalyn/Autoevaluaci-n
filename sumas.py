n=int(input("Introducir el valor de n: "))
m=int(input("Introducir el valor de m: "))

x=n
while x<=(n*m):
    if x%n==0:
        print(x)
    x=x+1
