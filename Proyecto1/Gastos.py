import random as rn

def Elementos_Comprados():
    elementos = [0,0,0,0,0,0,0,0,0,0]
    for i in range(len(elementos)):
        if elementos[0] == 0:
            elementos[i] = rn.randint(50,100)
        else:
            elementos[i] = rn.randint(int(elementos[i-1]*0.9),int(elementos[i-1]*1.1))
    return elementos

print(Elementos_Comprados())