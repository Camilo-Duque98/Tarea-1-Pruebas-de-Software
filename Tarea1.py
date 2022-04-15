import logging
import time

pila = []
def Stack():
    global pila
    word=input("Ingrese una palabra: ")
    if word in pila:
        logging.info(time.strftime('%H:%M:%S',time.localtime())+": Entrada "+word +" Valor obtenido")
    else:
        pila.append(word)
        logging.info(time.strftime('%H:%M:%S',time.localtime())+": Entrada "+word+" no permitido" )

def Show():

    global pila
    pila2=pila.copy()
    pila2.reverse()
    for i in pila2:
        print("{:<20}".format("---------------------"))
        print("|{:<20}|".format(i))

def Compare():
    
    word1= input("Ingrese la primera palabra a comparar: ")
    word2= input("Ingrese la segunda palabra a comparar: ")
    logging.info(time.strftime('%H:%M:%S',time.localtime())+":Entrada "+word1+", Entrada "+word2+", valor obtenido.")
    logging.info(time.strftime('%H:%M:%S',time.localtime())+":Inicio del proceso de comparación de las palabras")
    if word1 == word2:
        
        if word1 in pila :

            print("Las palabras son iguales")

        else:

            logging.error(time.strftime('%H:%M:%S',time.localtime())+": No se encuentra la palabra "+word1+" en la pila")
            print("Las palabras son iguales, pero no se encuentran en la pila\n")
    
    else:

        if word1 in pila and word2 in pila:

            logging.info(time.strftime('%H:%M:%S',time.localtime())+": Entrada "+ word1+", Entrada "+ word2+ ", no coinciden ")
            print("Las palabras no coinciden, pero si se encuentran en la pila")

        elif word1 in pila and word2 not in pila:
            logging.error(time.strftime('%H:%M:%S' ,time.localtime())+": La palabra "+ word2+ " no se encuentra en la pila.")
            print("La palabra "+word2+" no se encuentra en la pila")
        elif word1 not in pila and word2 in pila:
            logging.error(time.strftime('%H:%M:%S' ,time.localtime())+": La palabra "+ word1+ " no se encuentra en la pila.")
            print("La palabra "+word1+" no se encuentra en la pila")
        else:
            logging.error(time.strftime('%H:%M:%S', time.localtime())+": Entrada "+word1+", entrada "+word2+", no permitida, ya que no se encuentran en la pila ")
            print("Las palabras no se encuentran en la pila.")

def choice():
    print("Selccione una Opcion\n")
    print("1- Agregar Elementos a la pila\n")
    print("2-Mostrar elementos de la pila\n")
    print("3-Comparar elementos de la pila\n")
    print("4-Eliminar elemento de una pila\n")
    print("5-Salir\n")
    try:
        return int(input("Ingrese su opcion: "))
    except:
        return " "
        

def Delete():
    global pila
    try:
        logging.info(time.strftime('%H:%M:%S',time.localtime())+":Se elimino la palabra "+pila[len(pila)-1])
        pila.pop()
        print("Se elimino un elemento de la pila")
    except:
        print("La pila esta vacia")
        logging.error(time.strftime('%H:%M:%S', time.localtime())+": La pila esta vacia")

def main():
    while(1):
        
        logging.basicConfig(filename="test.log" , level="DEBUG")
        choicee = choice()
        
        if choicee == 1:
            logging.info(time.strftime('%H:%M:%S',time.localtime())+":Agregando elemento a la pila")
            Stack()
        elif choicee == 2:
            logging.info(time.strftime('%H:%M:%S',time.localtime())+":Se muestra los elementos de la pila")
            Show()
            logging.info(time.strftime('%H:%M:%S',time.localtime())+":La pila fue mostrada satisfactoriamente")
        elif choicee == 3:
            logging.info(time.strftime('%H:%M:%S',time.localtime())+":Se selecciono la opción de comparar")
            Compare()
        elif choicee == 4:
            Delete()
        elif choicee == 5:
            logging.info(time.strftime('%H:%M:%S',time.localtime())+": Finaliza el programa" )
            break
        else:
            logging.warning(time.strftime('%H:%M:%S',time.localtime())+": Entrada no permitida")
            print("Elección no permitida\n")
        
        print("{:<50}".format("----------------------------------------------------------------------------------------------------------------------------"))



if __name__=="__main__":
    main()