import numpy as np
vec=np.array([6,7,8,9,10])
e1=vec[0]
print("el elemento 1 de la posicion cero es: ",e1)#elemento en la posicion 0

#modificar valor de una posicion
vec[0]=5
print("ahora 5 es el primer elemento",vec)


#INDEXACION
#se envia un vector con una lista de indices que se quiere mostrar. Dando como resultado un nuevo vector con los elementos de esas posiciones
posiciones=np.array([0,4,1,3])
resultado=vec[posiciones]
print("vec con las posiciones del vector posiciones= ",resultado)

#ASIGANAR UN MISMO VALOR A VARIOS INDICES
print("vec= ",vec)
posiciones1=np.array([0,2])
vec[posiciones1]=10#tendremos al 10 en los idices del vector posiciones1
print("Vec= ",vec)


#EJERCCIO:mostrar los nombres de los estudiantes ordenadas de menor a mayor con respecto a su promedio
estudiante=np.array(["Axell","Paulette","Josue","Johana"])
promedio=np.array([9,1,10,7])

#argsort: retorna un vector de posiciones de los elementos de menor a mayor
posiciones=np.argsort(promedio)#-->retorna este vector---[1,3,0,2]
print("los estudiantes ordenados de menor a mayor son: ",estudiante[posiciones])