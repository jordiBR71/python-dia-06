mi_archivo = open('Jordi.txt')

print(mi_archivo)

#print(mi_archivo.read())

'''una_linea = mi_archivo.readline()
print(una_linea.upper())
una_linea = mi_archivo.readline()
print(una_linea)
una_linea = mi_archivo.readline()
print(una_linea)'''

#print(mi_archivo.readlines())

for l in mi_archivo:
    print (l)