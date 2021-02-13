def guardar_palabras(ruta_texto, ruta_palabras):  #Arreglar errores de ñ y de ª
    """Recibe donde esta el archivo texto y donde se van a guardar las palabras del archivo texto. Selecciona donde estan las palabras y las guarda en la segunda ruta"""

    lista_de_palabras = []  #lista de donde las va a guardar, ordenar y luego subirlas al archivo
    
    with open(ruta_texto, "r") as e:  #abre el texto
        linea = e.readline()
        
        while linea != "":  #Mientras el archivo no este vacio, lo ejecuta

            palabras_de_linea = linea.split("\n")
            palabras_de_linea = linea.split(" ")
    

            for palabra in palabras_de_linea: #Recorre cada palabra
                pal_a_subir = "" #Palabra que se va a subir a la lista
                anterior = ""
                for c in palabra:
                    
                    if c.isalpha(): #Si es letra y tiene acento, se lo cambia
                        c = c.lower()  
                        if c == "á":
                            pal_a_subir += "a"
                        elif c == "é":
                            pal_a_subir += "e"
                        elif c == "í":
                            pal_a_subir += "i"
                        elif c == "ó":
                            pal_a_subir += "o"
                        elif c == "ú":
                            pal_a_subir += "u"
                        else:
                            pal_a_subir += c
                            
                    else: #Si no es letra y habia una palabra anterior lo sube, sino lo ignora
                        if anterior.isalpha():
                            if not pal_a_subir in lista_de_palabras: #Se fija que no este en la lista
                        
                                lista_de_palabras.append(pal_a_subir)
                                
                            anterior = ""
                            pal_a_subir = ""
                    anterior = c
                
                if pal_a_subir != "":
                    
                    if not pal_a_subir in lista_de_palabras:   #Se fija que no este en la lista
                        
                        lista_de_palabras.append(pal_a_subir)

            linea = e.readline()

    lista_de_palabras = sorted(lista_de_palabras)
    
    with open(ruta_palabras, 'w') as s:  #abre el otro archivo, recorre la lista y va guardando las palabras

        for p in lista_de_palabras:

            s.write(p +'\n')



def generar_palabras(): #Arreglar errores de las ultimas palabras (no se si se agregan bien )

    
    guardar_palabras("Cuentos .txt", "palabras_cuentos_N.txt")
    guardar_palabras("La araña negra - tomo 1 .txt", "palabras_La araña negra - tomo 1 _N.txt")
    guardar_palabras("Las 1000 Noches y 1 Noche.txt", "palabras_Las 1000 Noches y 1 Noche_N.txt")

    with open("palabras.txt", "w") as palabras, open("palabras_cuentos_N.txt", 'r') as texto_1, open("palabras_La araña negra - tomo 1 _N.txt", 'r') as texto_2, open("palabras_Las 1000 Noches y 1 Noche_N.txt", 'r') as texto_3:


        palabra_1 = texto_1.readline().strip('\n')
        palabra_2 = texto_2.readline().strip('\n')
        palabra_3 = texto_3.readline().strip('\n')

        while palabra_1 != "" and palabra_2 != "" and palabra_3 != "" :  #Bucle hasta que los archivos esten vacios

            if palabra_1 == palabra_2 or palabra_1 == palabra_3: #Si hay palabras iguales, saltea una palabra en un archivo
                palabra_1 = texto_1.readline().strip('\n')
            if palabra_2 == palabra_3:
                palabra_2 = texto_2.readline().strip('\n')


            if palabra_1 < palabra_2 and palabra_1 < palabra_3:  #Elige la palabra menor, la escribe en el archivo, y lee la siguiente linea
                palabras.write(palabra_1 + '\n')
                palabra_1 = texto_1.readline().strip('\n')

            elif palabra_2 < palabra_3:
                palabras.write(palabra_2 + '\n')
                palabra_2 = texto_2.readline().strip('\n')

            else:
                palabras.write(palabra_3 + '\n')
                palabra_3 = texto_3.readline().strip('\n')
