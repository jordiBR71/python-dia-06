from os import system
from pathlib import Path
import time

ruta = Path('C:/Users/jotab/Desktop/Python Total/Día 06/Recetas')
system('cls')

print('Bienvenido al gestor de RECETAS')
time.sleep(1)

print('Las recetas están en la siguiente carpeta:\n\n',ruta,"\n")

recetas = 0
for txt in Path(ruta).glob('**/*.txt'):
      recetas +=1
print(f"Tienes {recetas} recetas")

time.sleep (1)
system('cls')

def leer_receta():
    print('1. Leer receta')


def crear_receta():
    print ('2. Crear receta')

def crear_categoria():
    print('3. Crear categoría')

def eliminar_receta():
    print('4. Eliminar receta')

def eliminar_categoria():
    print('5. Eliminar categoría')

def salir():
    print('6. Salir')

opciones = {
    '1' : ('Leer receta', leer_receta),
    '2' : ('Crear receta', crear_receta),
    '3' : ('Crear categoría', crear_categoria),
    '4' : ('Eliminar receta', eliminar_receta),
    '5' : ('Eliminar categoría', eliminar_categoria),
    '6' : ('Salir', salir)}

'''opciones=(1,2,3,4,5,6)'''
eleccion = None
def menu_principal():

    print('Elige una opción: \n\n',
             '1. Leer receta\n',
             '2. Crear receta\n',
             '3. Crear categoría\n',
             '4. Eliminar receta\n',
             '5. Elimnar categoría\n',
             '6. Salir')
    print(opciones)




while eleccion not in opciones.keys():
    menu_principal()
    eleccion = int(input("Opción: "))
else:
    print(f"Has escogido la opción {eleccion}")