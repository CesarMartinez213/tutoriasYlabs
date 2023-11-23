#Creación de un archivo binario

def main():
    #creación de un archivo binario con enteros
    print ("creación de un archivo binario")
    nombre_archivo= "enterosbinario.bin"
    f = open(nombre_archivo, "wb")
    resp = "s"
    while resp == "s":
        lista= [ 2, 3, 5, 7, 11, 13, 15]
        f.write (bytearray(lista))
        print ("guarde registro")
        resp = input ("desea continuar s/n ")    
    f.close()
    f = open(nombre_archivo, "rb")
    datos= f.read()
    print (datos.decode("utf-8"))
    print("**** ya acabe****")

#LLamada al programa principal
if __name__== "__main__":
    main()
