import numpy as np

#Ubicar un elemento mediante su posicion
m=np.arange(24).reshape(4,6)
print("la matriz m =",m)

print("Elemento de m en la posicion, f3, c4: ",m[3][4])#-->22

#ORDENAR los elementos de un vector de forma ascendente
#sort(vector/matriz)
vector1=np.array([7,8,9,5,4,3,90])
print(np.sort(vector1))

#np.POWER: eleva todos los elementos del vec o matriz a una determinada potencia
m3=np.array([2,4,5,7])
print("m3= ",m3)
print("el cubo de m3=",np.power(m3,3))

#potencia de vectores
m5=np.array([2,3,4,5,6,7])
print("el cuadrado de m3= ",m3**2)

#IDENTIFICACION DE LOS VALORES MEDIANTE UNA CLASIFICACION
print(np.array(m5>=4))#la condicion le indica que mire que elementos del vector es >=4
#>>[False False  True  True  True  True]

#ENCONTRAR EL VALOR MAXIMO
#FORMA1--->print(m6.max())---<class 'numpy.int32'>
#FORMA2---->print(np.array(m6.max()))-----<class 'numpy.ndarray'>

m6=np.array([2,3,4,5,6,7])
print("m6=",m6)
maximo=np.array(m6.max())
#print("el maximo de m6= ",np.array(m6.max()))
print("el maximo de m6= ",maximo)

#ENCONTRAR EL MINIMO
#FORMA1--->print(m6.min())---<class 'numpy.int32'>
#FORMA2---->print(np.array(m6.min()))-----<class 'numpy.ndarray'>

print("El minimo de m6= ",np.array(m6.min()))

#COMBINAR 2 vectores
vec1=np.array([2,3,4,5,6,7])
vec2=np.array([8,9,10,11,12,13])
print("vec1 combinada vec2= ",np.concatenate((vec1,vec2)))

#SUMAR 2 MATRICES
matriz1=np.array([[1,2],
                  [3,4]])
matriz2=np.array([[5,6],
                  [7,8]])
print("m1+m2=",matriz1+matriz2)#nos da una suma aritmetica

#SUMAR TODA LA MATRIZ CON UN VALOR
print("matriz 1+2= ",matriz1+2)#---[[3 4] [5 6]]

#FUNCION ADD: suma los elementos de matrices matriz1+matriz2
print("matriz1+matriz2 = ",np.add(matriz1,matriz2))

#FUNCION SUBTRACT: resta los elementos de una matriz
print("matriz1-matriz2 = ",np.subtract(matriz1,matriz2))#---[[-4 -4] [-4 -4]]

#FUNCION .DOT
#multiplicacion
#nombre_vec_m.dot(nombre_vec_m2)
matrizPrueba1=np.array([[1,2],[3,4]])
matrizPrueba2=np.array([5,6],[7,8])

