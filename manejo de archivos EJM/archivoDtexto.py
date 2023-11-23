#Este programa almacena datos en un archivo de texto y luego los lee y opera sobre ellos
#Creación de un archivo


print ("****Este programa almacena datos en un archivo de texto****")
print ("****luego los lee y opera sobre ellos ****")

f=open("filetexto.dat", "w")       # abro el archivo de modo escritura con "w"

print ("**** pide los datos de los estudiantes ****")
resp = "s"
while resp == "s":             # en un ciclo pido los datos 
    cedula = input ("ingrese la cédula del estudiante ")
    nombre = input ("ingrese la nombre del estudiante ")
    edad = input ("ingrese la edad del estudiante ")
    promedio = float( input ("ingrese el promedio del estudiante "))
    spromedio = str (promedio)              # convierto a strig un real
    
    f.write ( "{0}#{1}#{2}#{3}\n".format (cedula, nombre, edad, spromedio)) # guardo en el archivo
    resp = input ("desea continuar s/n ")

f.close()                    # cierro el archivo


#*********** recuperación de datos almacenados en el archivo ********
print (" ****** muestra de una sola vez el contenido del archivo *****")
f=open("filetexto.dat", "r")  # abro el archivo de modo lectura con "r"
print (f.read())                   # lectura de todo el contenido  del archivo


#*********** lectura linea por linea de los datos almacenados en el archivo ********
print (" ahora muestra el contenido linea por linea ")
f.seek(0)    # me posiciono en el primer registro


linea =  f.readline() # recorrido de los registros de un archivo usando un while
while linea != "":                    
    print(linea)
    linea =  f.readline()


#*********** otra forma de leer linea por linea de los datos del archivo **

print (" ahora muestra los campos separados y opera sobre ellos ")
f.seek(0)    # me posiciono en el primer registro
conta=0
suma_edad=0
for linea in f:                     #esta es otra manera de recorrer los registros en un archivo usando un for
    print(linea)
    lista_campos = linea.split('#')
    print ('imprimiendo campos')
    print (lista_campos)
    
    suma_edad = suma_edad + int(lista_campos[2])
    conta = conta +1

print ('el promedio de las edades es', suma_edad/conta)   
print ('este es el final')
