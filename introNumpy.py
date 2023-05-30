import numpy as np
#vector o arreglo 
#nombre_del_array=np.array([lista/coleccion/obj. iterable])
#donde se le envia a la funcion arraya el objeto iterable

#Array vacio
arr=np.array([])
print(arr)

#Array con elementos
arr1=np.array([1,2,3,5])
print(arr1)
#>>[1 2 3 5] se imprime sin sus comas. Siguen habiendo 5 elementos

#IMPORTANTE
# los vectores son similares a las listas, pero en VECTORES los elementos DEBEN SER del MISMO TIPO
vector=np.array([1,2,"juan",True,5])  #-->si los elementos del objeto iterable son de DISTINTOS TIPOS, NO va a votar un error
#Hara upcasting, es decir armonizara los elementos para que sean del mismo tipo del elemento PREDOMINIANTE

print(vector)#toodos los elementos llegaran a ser strings

#INDEXAR ELEMENTOS
#variable_guarda_elemento=nameArreglo[indice]
elemento=arr1[0]
print(f"elemento: {elemento}")

elemento2=arr1[1:3]#elemento2 sigue siendo una varible de tipo vector al mostrarlo en pantalla como uno
print(elemento2)#[2 3]


#Crear un arreglo a partir de un RANGE
#Range es un elemento iterable que genera una lista del 0-nelementos-1(deteminado por el numero que esta entre parentesis)

arreglo=np.array(range(10))#mostrara elementos del 0-9
print(f"El arreglo o vector con range es: {arreglo}")

#transformar todos los elmentos del range a flotantes
arreglo2=np.array(range(10),float)
print(arreglo2)#--->[0. 1. 2. 3. 4. 5. 6. 7. 8. 9.] estos son n flotantes, el cero despues de la coma no se pone


#Funcion ARANGE: es lo mismo que range, pero retorna un VECTOR, no una lista

#Arange(start=0 por defecto, stop=parametro que recibe, dtype=tipo de dato del arange )
arreglo1=np.arange(10)#se generara un vector del 0-9. 
print(f"funcion arange: {arreglo1}")

#transformar todos los elmentos del range a flotantes con ARANGE
arreglo3=np.arange(10,dtype=float)
#dtype=tipo-->funcion que requiere el nombre del tipo
print(f"arreglo 3: {arreglo3}")

#arange con saltos
arreglo4=np.arange(5,10)#vector del 5-9
print(f"el arreglo 4 es: {arreglo4}")

arreglo5=np.arange(2,10,2)#vector 2-8 con saltos de dos en dos
print(f"arreglo5: {arreglo5}")#[2 4 6 8]

#EXCEPCION: al haber ocupado todos los parametros YA NO ES NECESARIO mandar dtype
arreglo6=np.arange(2,10,2,float)#vector 2-8 con saltos de dos en dos donde sus elementos son flotantes
print(f"Arreglo6: {arreglo6}")#[2. 4. 6. 8.]

 #FUNCION ZEROS
#manda la cantidad de ceros que tendra el vector como parametro
#IMPORTANTE: por defecto son flotantes
arrZero=np.zeros(5)
print(f"arreglo de 5 ceros: {arrZero}")

#PERMITE CAMBIAR EL TIPO DE DATO
arrZero1=np.zeros(5,int)#transforma los cinco ceros a enteros. No es necesario usar dtype
print(f"arrZero 1={arrZero1}")

#FUNCION ONES
arrOnes=np.ones(5)#el vector tendra el numero de "unos" como parametro
#IMPORTANTE: por defecto son flotantes
print(f"arrOnes: {arrOnes}")#[1. 1. 1. 1. 1.]

#PERMITE CAMBIAR EL TIPO DE DATO
arrOnes1=np.ones(5,int)#transforma los cinco unos a enteros. No es necesario usar dtype
print(f"arrOnes1 = {arrOnes1}")#[1 1 1 1 1]

#RELLENAR VECTORES CON CUALQUIER NUMERO
vectorOnes=np.ones(6,int)

vectorOnes.fill(2)#rellena un vector creado con el numero del parametro.
#sustituye la misma cantidad de elementos por el numero del parametro con el tipo de dato del arreglo original
#si el vector de unos tiene flotantes por defecto, fill los conservara ese tipo de dato y el numero que sustituye los elementos tambien flotante
print("el vectorOnes tiene ahora: ",vectorOnes)


#sumar individualmente a los elementos matriz
vector2=np.array([8,5,6,9])
print(f"vector2: {vector2}")
vector2+=np.array([5])
print(f"vector2 +5 a cada uno: {vector2}")

#multiplicar entre dos vectores
vector3=np.array([1,2,3,4])
print("vector 3: ",vector3)
vector4=np.array([5,6,7,8])
print("vector 4: ",vector4)
print("el vector 3*4: ",vector3*vector4)