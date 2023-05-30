import numpy as np
m=np.array([[1,-1,2],[3,2,0]])
print("m=",m)

#Generar una matriz de una sola columna
m1=np.arange(1,4).reshape(3,1)
print("m1=",m1)

#MATRIZ TRANSPUESTA
#Se obtiene cambiando sus filas por columnas o viceversa
#FUNCION np.transpose
m1Trasnpuesta=np.transpose(m1)
print("m1 transpuesta es= ",m1Trasnpuesta)


#SISTEMAS DE ECUACIONES
#Ax=b
'''
A=  2 1 -2      B= -3
    3 0  1          5
    1 1 -1          -2
'''
#cuanto vale x??
#Paso 1: realizar matriz A

a=np.array([[2,1,-2],[3,0,1],[1,1,-1]])

print("A=",a)
print()

#Paso 2: realizar matriz B
b=np.array([[-3],[5],[-2]])
print("B=",b)
print()

#Paso 3: tranponer b
