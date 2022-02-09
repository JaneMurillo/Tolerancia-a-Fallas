# Python
# Otras herramientas para el manejo de errores

while True:
  
  try:
    entero = int(input("Ingresa un numero entero: "))
  
  except ValueError:
    print ("Error")

  except TypeError:
    print ("Tipo de dato invalido")

  else:
    print(entero)

  finally:
    print("Se ha ejecutado el programa\n")
