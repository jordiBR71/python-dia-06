from pathlib import Path, PureWindowsPath
carpeta = Path('C:/Users/jotab/Desktop/Python Total/Día 06/Dia 06 alternativo/nuevo archivo.txt')

print(carpeta.read_text())

print(carpeta.name)
print(carpeta.stem)
print(carpeta.suffix)


if not carpeta.exists():
    print('el archivo no existe')
else:
    print('sí, el archivo existe')

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)
