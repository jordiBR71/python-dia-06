from pathlib import Path
ruta_base = Path.home()
print(ruta_base)

ruta = Path(ruta_base,'desktop','Python Total','Día 6')
print(ruta)

ruta_2 = Path(ruta, 'Jordi.txt')
print(ruta_2)