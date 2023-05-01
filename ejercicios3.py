def abrir_leer(archivo):
    archivo = open('ejemplo.txt')
    return archivo.read()

def sobreescribir(archivo):
    archivo_sobreescribir = open(archivo,'w')
    archivo_sobreescribir.write('contenido eliminado')

def registro_error(archivo):
    log_errores = open(archivo, 'a')
    log_errores.write('se ha registrado un error de ejecución')