import numpy as np
#DECLARAR UNA MATRIZ
matriz=np.array([[1,2,3],
                 [4,5,6]])#los [] externos representan toda la matriz, los internos las filas de las matrices
print("matriz 2*2:",matriz)

#Pasar como argumento una lista
lista=[1,2,3,4,5]
vector=np.array(lista)
print(vector)

#Pasar como argumento una lista anidada para formar una matriz
matriz33=[[1,2,3],[4,5,6],[7,8,9]]
m3=np.array(matriz33)
print("la matriz 3*3: ",m3)

#GENERAR MATRICES CON ELEMENTOS EN ORDEN ASCENDENTE 
#RESHAPE: en conjunto con la funcion arange que genera una coleccion ficticia de n elementos del 0-nelementos-1
m=np.arange(15).reshape(3,5)#RESHAPE, toma como argumentos las filas y columnas a crear con los n elementos del arange
print("matriz 3*5 = ",m)

#los elementos generados con el arange deben coincidir con el numero de filas y columnas que establece el reshape.
#m=np.arange(15).reshape(4,5)--->esto saldra ERROR por que 4*5=20 y los elementos que genera arange es 15 y /=20

#FUNCIO SHAPE: determina el numero de FILAS y COLUMNAS de una matriz(en ese orden)
m1=np.arange(20).reshape(4,5)
print("los filas y columanas de m1 son: ",m1.shape)

#FUNCION .ndim: brinda el numero de ejes o dimensiones que posee una matriz
print("la dimensiones de m1 son: ",m1.ndim)#-->2 dimensiones porque es una matriz

#FUNCION SIZE: numero total de elementos
m2=np.arange(10).reshape(5,2)
print("matriz 5*2: ",m3)
print("el numero de elementos de m2: ",m2.size)

#FUCION ZEROS
m3=np.zeros((4,2),int)
print("matriz de ceros 4*2: ",m3)

#FUNCION LINSPACE
m4=np.linspace(99,88)#el argumento es el primer y el ultimo elemento de la matriz 
print("matriz del 88-99: ",m4)#los numeros que esten entre 99-88 siguen una secuencia aletoria
print("el numero de elementod de m4 es: ",m4.size)
#tercer arguemento: determina cuantos elementos tendra el vector
m5=np.linspace(99,88,25)
print("m5 = ",m5)
print("el numero de elementos m5 es: ",m5.size)

#-------------------------------------------------------------------------
#matrices de 3 dimensiones
m3d=np.arange(24).reshape(2,3,4)#el primer argumento es el num de matrices, el segundo el num de filas que comparten las matrices y el tercero el numero de columnas
print("la matriz 3d de 3 filas y 4 columnas: ",m3d)

#ejemplo
m3d_tres_por_tres=np.arange(27).reshape(3,3,3)#como son tres matrices de 3*3 el numero de elementos que alojara la matriz=29--->3m*3f*3c=27e
print("m3d_tres_por_tres = ",m3d_tres_por_tres)
