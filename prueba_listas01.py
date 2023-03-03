from listas_2022 import *

#Creacion instancia
lista_01 = SimpleList()

print("Lista:",lista_01)
print("Esta Vacia:",lista_01.EmptyList())

#Adicion elementos
lista_01.AddToBeginning(1)
lista_01.AddToBeginning(2)
lista_01.AddToBeginning(3)
print("Lista:",lista_01)
print("Esta Vacia:",lista_01.EmptyList())

#Buscar elementos
print("Buscar 01:",lista_01.Search(5))
print("Buscar 02:",lista_01.Search(1))

#Eliminar Al inicio
print("Eliminar 01:",lista_01.RemoveFirst())
print("Lista:",lista_01)
