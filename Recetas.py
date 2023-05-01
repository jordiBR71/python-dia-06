import os
from pathlib import Path
from os import system

mi_ruta = Path(Path.home(), "Recetas")

def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador +=1
    
    return contador

    
# mostrar menú inicio

def inicio():
    system('cls')
    print ('*' * 31)
    print('*'* 2 + "  Bienvenido al RECETARIO  " +'*' * 2)
    print('*' * 31)
    print('\n')
    print(f"Las recetas se encuentran en {mi_ruta}")
    print(f"Total de recetas: {contar_recetas(mi_ruta)}")

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print('Elige una opción')
        print('''
        [1] - Leer receta
        [2] - Crear nueva receta
        [3] - Crear nueva categoría
        [4] - Eliminar receta
        [5] - Eliminar categoría
        [6] - Salir del programa''')
        eleccion_menu = input()
    
    return int(eleccion_menu)

    

# mostrar categorías

def mostrar_categorias(ruta):
    print("Categorias:")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador +=1
    return lista_categorias

# elegir categorías

def elegir_categorias(lista):
    eleccion_correcta = 'x'

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range (1, len(lista)+1):
        eleccion_correcta = input('\nElige una categoría: ')
    
    return lista[int(eleccion_correcta)-1]


# mostrar recetas

def mostrar_recetas(ruta):
    print ('Recetas: ')
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"{[contador]} - {[receta_str]}")
        lista_recetas.append(receta)
        contador +=1
    
    return lista_recetas

# elegir receta

def elegir_recetas(lista):
    eleccion_receta = 'x'

    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range (1, len(lista)+1):
        eleccion_receta = input('\nElige una receta: ')
    
    return lista[int(eleccion_receta)-1]

# leer receta

def leer_receta(receta):
    print(Path.read_text(receta))

# crear receta

def crear_receta(ruta):
    existe = False

    while not existe:
        print('\nEscribe el nombre de tu receta: ')
        nombre_receta = input() + '.txt'
        print('\nEscribe tu nueva receta: ')
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f'Tu receta {nombre_receta} ha sido creada')
            existe = True
        else:
            print('Lo siento, esa receta ya existe')
        

# crear categoria

def crear_categoria(ruta):
    existe = False
    
    while not existe:
        print('\nEscribe el nombre de la nueva categoría: ')
        nombre_categoria = input() 
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f'Tu nueva categoría {nombre_categoria} ha sido creada')
            existe = True
        else:
            print('Lo siento, esa categoría ya existe')

# eliminar receta

def eliminar_receta(receta):
    Path(receta).unlink
    print('\nLa receta {receta.name} ha sido eliminada')

# eliminar categoria

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print('\nLa categoría {categoria} ha sido eliminada')

# volver al inicio

def volver_inicio():
    eleccion_regresar = 'x'

    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input(f'Presione V para volver al menú: ')




finalizar_programa = False

while not finalizar_programa:

    menu = inicio()

    if menu == 1:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categorias(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print("Esta categoría no tiene recetas. Elige otra")
        else:
            mi_receta = elegir_recetas(mis_recetas)
            leer_receta(mi_receta)
        volver_inicio()
        

    elif menu == 2:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categorias(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()
        
    elif menu == 3:
        crear_categoria(mi_ruta)
        volver_inicio()
        

    elif menu == 4:
        mis_categorias = mostrar_categorias(mi_ruta)
        if len(mis_categorias) < 1:
            print('No tienes categorías. Crea una.')
        else:
            mi_categoria = elegir_categorias(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_recetas(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()
        

    elif menu == 5:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categorias(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()
        

    elif menu == 6:
        finalizar_programa=True