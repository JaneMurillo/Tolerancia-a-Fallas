import psutil, sys
import pickle
import os, time
from pathlib import Path

# Verificacion del estado de la aplicación

import sys
import psutil

def revisar_argumentos():
# Evitar errores
    if len(sys.argv) == 1:
    	print('Este programa no funciona sin argumentos')
    	sys.exit(0)

def objetivos():
# Mediante argumentos se recibe el nombre del proceso que se va a interceptar
    targets = sys.argv[1:]
    i = 0
    while i < len(targets):
    	if not targets[i].endswith('.exe'): # Para aceptar argumentos con .exe
    		targets[i] = targets[i] + '.exe'
    	i += 1
    return targets

def bloquear(target):
    for proc in psutil.process_iter():
    	if proc.name().lower() == target.lower():
    		proc.kill() # Mata el proceso

if __name__ == '__main__':
    revisar_argumentos()
    targets = objetivos()
    while True:
    	for target in targets:
    		bloquear(target)

# Aplicación PyNotes

app = True

while app == True:
    os.system("cls")
    print("\t\t\tP Y N O T E\n\nBienvenido a la aplicación de notas de Python\n")
    print("Notas actuales:")
    print(os.listdir()) 

    print("\n1. Añadir nueva nota\t2. Mostrar nota\t  3. Editar nota\t  4. Salir\n")
    opc = input ("Escoge una opción: ")

    if(opc == '1'):
        print("\n\t\t AÑADIR NOTA")
        print("Editando...")
        notetitle = input("Titulo de la nota: ")
        fileread = open(notetitle, 'ab')
        content = input("Escribe el contenido de la nota: ")
        pickle.dump(content, fileread)
        print("Guardando...")
        time.sleep(3)
        fileread.close()
        
    elif(opc == '2'):
        print("\n\t\t MOSTRAR NOTA")
        print("Notas actuales:")
        print(os.listdir()) 
        filename = input("\nEscribe el nombre del archivo que quieres abrir: ")
        try:
            fileread = open(filename, 'rb')
            while True:
                try:
                    note = pickle.load(fileread)
                    print("\n\t\tN O T A") 
                    print("\nTitulo: ", filename)
                    print("Contenido:", note)
                    print("\n")
                    os.system("pause")
                    break
                except:
                    break
            fileread.close()
        except:
            print("Ocurrió un error: no existe ese archivo.\n")
            os.system("pause")

    elif(opc == '3'):
        print("\n\t\t EDITAR NOTA")
        print("Notas actuales:")
        print(os.listdir()) 
        filename = input("\nEscribe el nombre del archivo que quieres editar: ")
        fileopc = int(input("Editar: 1. Titulo  2. Contenido. Escoge 1 o 2: "))
        if(fileopc == 1):
            try:
                newtitle = input("Escribe el nuevo nombre del archivo: ")
                path_actual = Path(filename)
                path_objetivo = Path(newtitle)
                Path.rename(path_actual,path_objetivo)
            except:
                print("Ocurrió un error: no existe ese archivo.\n")
                os.system("pause")
        elif(fileopc == 2):
            try:
                os.remove(filename)
                fileread = open(filename, 'ab')
                while True:
                    try:
                        print("\n\t\tN O T A") 
                        print("\nTitulo: ", filename)
                        print("Contenido: ")
                        newcontent = input("\nEscribe el contenido de la nota: ")
                        pickle.dump(newcontent, fileread)
                        print("\n")
                        os.system("pause")
                        print("Guardando...")
                        time.sleep(3)
                        fileread.close()
                        break
                    except:
                        break
            except:
                print("Ocurrió un error: no existe ese archivo.\n")
                os.system("pause")
        
    elif(opc == '4'):
        print("\nHasta pronto!\n- PYNOTES\n")
        app = False

    else:
        print("Opción no valida\n")
        time.sleep(2)