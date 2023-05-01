from pathlib import Path


'''base = Path.home()

guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada Familia.txt"))

print(base)
print(guia)
guia2 = guia.with_name("La Pedrera.txt")
print(guia2)

print(guia.parent)
print(guia.parent.parent)'''

'''guia = Path (Path.home(), "Europa")

for txt in Path(guia).glob("**/*.txt"):
    print(txt)'''


guia = Path("Europa", "España", "Barcelona", "Sagrada Familia.txt")

en_europa = guia.relative_to("Europa")
en_espanya = guia.relative_to("Europa", "España")

print(en_europa)
print(en_espanya)