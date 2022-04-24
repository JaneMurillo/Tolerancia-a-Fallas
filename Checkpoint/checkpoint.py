import pickle
import os
from pathlib import Path
import time

"""
# Pequeño ejemplo del uso de Pickle
def savepickle():
    ListMonth = ["enero", "febrero", "marzo"]
    FileBin = open("FileList", "wb")
    pickle.dump(ListMonth, FileBin)
    FileBin.close()

def readpickle():
    try:
        with open('FileList', 'rb') as fileread:
            fileread = open ("FileList", "rb")
            picklefile = pickle.load(fileread)
            fileread.close()
    except PickleError:
        print("No se  guardó")"""
        
# Aplicación PyNotes
"""
app = True
notes = list()

while app == True:
    os.system("cls")
    print("\t\tP Y N O T E\n\nBienvenido a la aplicación de notas de Python\n")
    print("Notas actuales:")
    try:
        fileread = open('NotesPickle', 'rb')
        while True:
            try:
                note = pickle.load(fileread)
                notes.append(note)
                i=1
                for x in notes:
                    print("Nota ", i,":")
                    print(x)
                    i+=1
                break
            except:
                break
        fileread.close()
    except:
        print("No existe\n")

    print("1. Añadir nueva nota\t2. Editar nota\t3. Eliminar nota\t4. Salir\n")
    opc = input ("Escoge una opción: ")

    if(opc == '1'):
        print("Editando...")
        note = input("Contenido: ")
        fileread = open('NotesPickle', 'ab')
        pickle.dump(note, fileread)
        fileread.close()
        notes.append(note)

        
    elif(opc == '2'):
        print("Editando...")
        i=1
        for x in notes:
            print("Nota ", i,":")
            print(x)
            i+=1
        editnotenum = int(input("Escoge el número de nota a editar: "))
        print("\n")
        newcontent = input("Escribe el nuevo contenido: ")
        fileread = open('NotesPickle', 'ab')
        pickle.dump(note, fileread)
        fileread.close()
        notes.insert(editnotenum, newcontent)
        

    elif(opc == '3'):
        i=1
        for x in notes:
            print("Nota ", i,":")
            print(x)
            i+=1
        editnotenum = input("Escoge el número de nota a eliminar: ")
        notes.pop(editnotenum)
        
    elif(opc == '4'):
        print("\nHasta pronto!\n- PYNOTES\n")
        app = False

    else:
        print("Opción no valida\n")
        time.sleep(2)"""

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