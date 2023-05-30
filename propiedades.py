import numpy as np
a= np.array([12,23,45,78], float)

#PROPIEDADES
#dyte: retorna propiedades, las cuales son caracteristicas sobre un tipo de dato en concreto 
print("tipo= ",a.dtype)

#nomVec/M.ndim: Numero de dimensiones

#nomVec/M.shape: numero de filas y columnas en una tupla 

#nomVec/M.size: numero de elementos del vec o matriz


#FUNCIONES Y METODOS
#np.sum()  -->funcion, el parametro es el vector
#nombreVec/M.sum()---->metodo sin parametro por lo general

#suma de elementos
#vectores
suma=np.sum(a)#-->suma todos los elementos en el vector a
print("la suma de todos los elementos de a= ", suma)

#Matrices
m=np.arange(6).reshape(2,3)
print("la suma de todos los elementos es: ",m.sum())#--->15

#PRODUCTO DE TODOS LOS ELEMENTOS
vec=np.array([1,23,4,5,7,4])
print("el producto de todos los elementos de vec= ",vec.prod())

#PROMEDIO DE TODOS LOS ELEMENTOS: suma todos los elementos del vector y el total los divide para el numero de elementos
vec1=np.array([2,45,67,7,6,4,6,2])
print("el promedio de vec es: ",vec.mean())#--->8.25
print("el promedio de vec1 es: ",np.mean(vec1))#--->25.4

#Minimo Valor
print("el valor minimo de vec: ",np.min(vec))#--->1
print("el valor minimio de vec1: ",vec1.min())#--->2

#MAXIMO VALOR
maximo=np.max(vec)
print("el valor maximo de vec: ",maximo)#--->23
print("el valor maximo de vec1: ",vec1.max())#--->67

#POSICION DEL MINIMO VALOR
#forma1-funcion
print("la posicion del minimo valor de vec: ",np.argmin(vec))
#forma2-metodo
print("la posicion del maximo valor de vec1 es: ",vec1.argmin())

#POSICION DEL MAXIMO VALOR
#forma1-funcion
print("la posicion del maximo valor de vec es: ",np.argmax(vec))
#forma2-metodo
print("la posicion del maximo valor de vec1 es: ",vec1.argmax())

#ELEMENTOS UNICOS Y ORDENA DE MENOR A MAYOR: quita los elementos repetidos y los retorna ordenados
#FUNCION .UNIQUE-NO HAY METODO
print("el vector sin elementos repetidos es: ",np.unique(vec))
print("el vector1 sin elementos repetidos es: ",np.unique(vec1))

#ORDENA DE MENOR A MAYOR
print("vec de mayor a menor= ",np.sort(vec))
vec1.sort()
print("vec de mayor a menor= ",vec1)

#IMPORTANTE 
'''
sort y unique como funciones, PUEDEN SER ALMACENADOS EN UNA VARIABLE
ordenado=np.sort(vec)
E IMPRIMIRSE DIRECTAMENTE
print(np.unique(vec1))

como metodos NO me retornan nada, por lo tanto, NO PUEDEN SER ALMACENADOS EN UNA VARIABLE
PERO SE PUEDE HACER LO SIGUIENTE

vec.sort()
print(vec)--->se imprimira ya ordenado

vec1.unique()
print(vec1)---->se imprimira el vector con elementos unicos y menor a mayor
'''

#ORDENAR DE MENOR A MAYOR LOS INDICES
#vec=np.array([1,23,4,5,7,4])
vec2=np.array([2,43,51,10,9,40,8,2])

posiciones=np.argsort(vec)
print("los indices de los elementos de menor a mayor",posiciones)#si 1 es el menor con indice 0, el indice cero se imprimira
#----[0 2 5 3 4 1]
print("los indices de los elementos de menor a mayor son: ",vec2.argsort())#---[0 7 6 4 3 5 1 2]


#DESVIACION ESTANDAR
print("La desviacion estandar es: ",np.std(vec))
print("la desviacion estandar es: ",vec1.std())

#VARIANZA
varianza=vec1.var()
print("la varianza es: ",varianza)
print("la varianza de vec: ",np.var(vec))

#PRODUCTO PUNTO
print("producto punto= ",np.dot(vec,vec))

#RAIZ CUADRADA: DE TODOS LOS ELEMENTOS DEL VECTOR
print("raiz cuadrada: ",np.sqrt(vec))
print("raiz cuadrada vec1: ",np.sqrt(vec1))#no hay metodo

#VALORES ABSOUTOS: pasa todos los elementos a positivos
print("valores absolutos: ",np.abs(vec))
print("valores absolutos: ",np.abs(vec1))

#COPIA DEL VECTOR
print("el vec= ",vec)
print("el vec2.0= ",np.copy(vec))
vec1copia=vec1.copy()
print("copia de vec1= ",vec1copia)

