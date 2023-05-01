from importlib.resources import path
import os

ruta = os.getcwd()
print (ruta)
ruta = os.chdir('C:\\Users\\jotab\\Desktop\\Python Total\\Día 06\\Dia 06 alternativo')
ruta = os.getcwd()
print (ruta)



archivo = open('nuevo archivo.txt')
print(archivo.read())
#ruta = os.makedirs('C:\\Users\\jotab\\Desktop\\Python Total\\Día 06\\Dia 06 alternativo\\Otra carpeta')

#os.rmdir('C:\\Users\\jotab\\Desktop\\Python Total\\Día 06\\Dia 06 alternativo\\Otra carpeta')
ruta = ('C:\\Users\\jotab\\Desktop\\Python Total\\Día 06\\Dia 06 alternativo\\Otra carpeta.txt')
directorio = os.path.dirname(ruta)
archivo = os.path.basename(ruta)
print(directorio, '/',archivo)
print()
tupla = os.path.split(ruta)
print(tupla)

from pathlib import Path
carpeta = Path('C:\\Users\\jotab\\Desktop\\Python Total\\Día 06\\Dia 06 alternativo')
archivo = carpeta / 'nuevo archivo.txt'
mi_archivo = open(archivo)
print(mi_archivo.read())
