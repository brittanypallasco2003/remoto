import numpy as np
#los numeros aletorios no se pueden predecir logicamente

#retorna un numero aletorio entero
vector =np.random.randint(10)#retorna un numero aletorio del 0-10

#retorna n numeros aletorios en
vec1=np.random.randint(10,size=(5))
print(vec1)

#retorna n numeros aletorios para una matriz
matriz=np.random.randint(10, size=(3,3))#el parametro size recoge las filas y columnas, la multiplicacion de las dos NO SOBRESPASA los numeros aleatorios

#RETORNA N NUMEROS ALEATORIO FLOTANTE PARA UN VECTOR 
v1=np.random.rand(5)#5: parametro que determina el numero de elementos flotantes del vector
print("v1=",v1)#--->[0.03869649 0.27420135 0.22028412 0.89372202 0.08011959]

#RETORNA N NUMEROS ALEATORIOS FLOTANTES PARA UNA MATRIZ
m2=np.random.rand(2,2)#los argumentos del rand son el numero de filas y columnas
print("m2=",m2)

#RETORNA un valor de uno de los elementos del vector o matriz
v3=np.random.choice([1,2,3,5,78,6])
print("el elemento aleatorio= ",v3)

#RETORNA UNA MATRIZ DE ELEMENTOS ALEATORIOS DE UN VECTOR CON N FILAS Y N COLUMNAS
m3=np.random.choice([3,5,7,9,1], size=(2,3))
print("m3= ",m3)

#DISTRIBUCION ALEATORIA
#Conjunto de numeros aleatorios que siguen una determinada funcion de densidad de probabilidad

#Ejerccio:
#Genere una matriz que contenga 50 valores donde cada valor debe ser 4,2,8, o 10
m4=np.random.choice([2,4,8,10],p=[0.3,0.5,0.1,0.1], size=(50))#donde la primera matriz esta formada con los elementos que se piensa extraer 
#la otra matriz son los datos de probabilida

print("m4 tiene 50 elementos= ",m4)