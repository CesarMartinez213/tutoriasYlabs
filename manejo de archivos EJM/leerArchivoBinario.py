#Lectura de un archivo binario

def main():
    #lectura del cotenido de  un archivo binario 
    print ("lectura del contenido de un archivo binario")
    nombre_archivo= "enterosbinario.bin"
    f = open(nombre_archivo, "rb")    # abrirlo para lectura con rb
    numeros = list (f.read())
    print ()
    print (numeros)
    print("**** ya acabe****")

if __name__== "__main__":
    main()
