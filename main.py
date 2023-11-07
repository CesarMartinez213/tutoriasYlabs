from os import system

while(True):
    print("**************************")
    print(" Menu desplegable ")
    print(" Ingrese la opción correspondiente ")
    print(" a.  Mostrar lista de palabras en orden descendente por tamaño y dada una vocal")
    print(" b. Insertar en arreglo las palabras de longitud impar y cuyo caracter del medio no sea una vocal")
    print(" c. Cambiar subcadena por asteriscos")
    print(" d. Borrar todas las palabras con unas subcadena dada")
    print(" e. Salir")
    print("**************************")
    print()
    cadenaUsuario = str(input("Ingrese la cadena que desea procesar "))
    opcion = str(input("Ingrese la opción que desea ejecutar "))
    if( opcion == "a"):
        palabrasCadena = cadenaUsuario.split()
        vocalPalabraABuscar = str(input("Ingrese la vocal que desea buscar "))
        contador = 0
        listaPalabras = []
        for palabra in palabrasCadena:
            contador = 0
            for caracter in palabra:
                if caracter in vocalPalabraABuscar:
                    contador = contador + 1
            if(contador >= 3):
                listaPalabras.append(palabra)

        print("El arreglo de ordenado de palabras es: ")
        listaOrdenada = sorted(listaPalabras, key=len, reverse=True)
        if(len(listaOrdenada) > 0 ):
            print(listaOrdenada)
        else:
            print("No hay palabras con las vocal buscada con 3 o más repeticiones")

        print("Presione ENTER para continuar...")
        entrada = input()
        system("cls")

    elif opcion == "b":
        palabrasCadena = cadenaUsuario.split()
        listaPalabras = []
        for palabra in palabrasCadena:
            if((len(palabra) % 2 != 0) and (palabra[len(palabra) // 2] not in "aeiouAEIOU")):
                listaPalabras.append(palabra)

        print("Se encontrado un total de ", len(listaPalabras), " que cumplen la condicion")
        print("la lista es: ")
        print(listaPalabras)
        print("Presione ENTER para continuar...")
        entrada = input()
        system("cls")
    elif opcion == "c":
        subcadenaBuscada = str(input("Ingrese la subcadena que desea reemplazar: "))
        if(cadenaUsuario.find(subcadenaBuscada) == -1):
            print("La subcadena no existe dentro de la cadena dada")
        else:
            cadenaReemplazada = cadenaUsuario.split()
            for i, palabra in enumerate(cadenaReemplazada):
                if(palabra == subcadenaBuscada):
                    cadenaReemplazada[i] = "*"*len(palabra)
            cadena = ""
            for palabra in cadenaReemplazada:
                cadena = cadena + palabra + " "
            print(f'{cadena}')
        print("Presione ENTER para continuar...")
        entrada = input()
        system("cls")
    elif opcion == "d":
        subcadenaBuscada = str(input("Ingrese la subcadena que desea eliminar"))
        listaPalabrasEliminadas = []
        if(cadenaUsuario.find(subcadenaBuscada) == -1):
            print("La subcadena no existe dentro de la cadena dada")
        else:
            listaPalabras = cadenaUsuario.split()
            for i, palabra in enumerate(listaPalabras):
                if palabra.find(subcadenaBuscada) != -1:
                    listaPalabrasEliminadas.append(palabra)
                    del listaPalabras[i]
            cadena = ""
            for palabra in listaPalabras:
                cadena = cadena + palabra + " "
            print("La cadena con las palabras eliminadas es: " + cadena)
            print("Las palabras eliminadas fueron: ")
            for palabra in listaPalabrasEliminadas:
                print(palabra, len(palabra))
        print("Presione ENTER para continuar...")
        entrada = input()
        system("cls")
    elif opcion == "e":
        break
    else:
        print(" ----- Inserte una opción valida ----- ")
        print("Presione ENTER para continuar...")
        entrada = input()

