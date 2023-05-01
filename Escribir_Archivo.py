archivo = open('Jordi.txt','w')
'''archivo.write('Hola')
archivo.write('Jordi')'''

lista = ['Hola', 'Jordi', '¿cómo estás?']

for l in lista:
    archivo.writelines(l + '\n')

archivo.close()

archivo = open('Prueba.txt','a')
'''archivo.write('Hola')
archivo.write('Jordi')'''

lista = ['Hola', 'Jordi', '¿cómo estás?']

for l in lista:
    archivo.writelines(l + '\n')

print(archivo)

archivo.close()