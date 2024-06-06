def hola(a,b,c):
    if a + b > c:
        print("La suma es mayor que",c)
    else:
        print("La suma es menor que",c)
    return a + b
a=2
b=3
c=7

x=hola(a,b,c)
print(x)