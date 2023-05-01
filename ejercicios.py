archivo = open('mi_Archivo.txt','w')
archivo.write('Este es el Nuevo texto')
archivo.close()
archivo = open('mi_Archivo.txt')
print(archivo.read())
archivo.close()



archivo = open('mi_archivo.txt', 'a')
archivo.writelines(["Nuevo inicio de sesión","\n"])
archivo.close()
archivo = open('mi_archivo.txt')
print(archivo.read())
archivo.close()




registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

registro = open('registro.txt', 'a')
for r in registro_ultima_sesion:
    registro.write(r + '\t')
registro.close()
registro = open('registro.txt')
print(registro.read())
registro.close()