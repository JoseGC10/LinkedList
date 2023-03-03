from listas_2022 import *

lista_02 = SimpleList()
lista_02.AddToBeginning(10)
lista_02.AddToBeginning(20)
lista_02.AddToBeginning(30)
lista_02.AddToBeginning(50)
lista_02.AddToBeginning(50)
lista_02.AddToBeginning(50)
print("Lista 02:", lista_02)
#Eliminar por información
print("Eliminar 01:",lista_02.RemoveInfo(50))
print("Lista 02:", lista_02)
print("Eliminar 02:",lista_02.RemoveInfo(40))
print("Lista 02:", lista_02)
print("Eliminar 03:",lista_02.RemoveInfo(10))
print("Lista 02:", lista_02)
print("Eliminar 04:",lista_02.RemoveInfo(60))
print("Lista 02:", lista_02)

# Adicionar al final
print("Append: ", lista_02.Append(90))
print(lista_02)

# Eliminar al final
lista_03 = SimpleList()
lista_03.AddToBeginning(10)
lista_03.AddToBeginning(20)
lista_03.AddToBeginning(30)
lista_03.AddToBeginning(20)
lista_03.AddToBeginning(40)
print(lista_03)
print("RemoveLast: ", lista_03.RemoveLast())
print(lista_03)

# Reconteo de datos
print("Counter: ", lista_03.dataCount(20))

# Elemento al indicar una posición
print("ElementPos: ", lista_03.ElementPos(3))


