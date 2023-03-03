#Clase Nodo Simple
class SingleNode:
    #Constructor
    def __init__(self, data):
        self.data = data
        self.next = None
    #Str
    def __str__(self) -> str:
        return str(self.data)
    #Eq
    def __eq__(self, other):
        if not isinstance(other, SingleNode):
            return False
        return self.data == other.data
#Clase ListaSimple
class SimpleList:
    #Constructor
    def __init__(self) -> None:
        self.first = None
    
    #Lista Vacia
    def EmptyList(self):
        return self.first == None

    #Adicionar al inicio
    def AddToBeginning(self, new_data):
        NewNode = SingleNode(new_data)
        if self.EmptyList():
            self.first = NewNode
        else:
            NewNode.next = self.first
            self.first = NewNode
    
    #Eliminar al inicio
    def RemoveFirst(self):
        if self.EmptyList():
            return None
        else:
            data = self.first.data
            self.first = self.first.next
            return data
    
    #Buscar por dato
    def Search(self, data_sought):
        if self.EmptyList():
            return False
        else:
            currentNode = self.first
            while currentNode != None:
                if currentNode.data == data_sought:
                    return True
                currentNode = currentNode.next
            return False
    
    #Recorrido (Str)
    def __str__(self):
        string = "["
        currentNode = self.first
        while currentNode != None:
            string += str(currentNode.data) + " "
            currentNode = currentNode.next
        string += "]"
        return string
    
    #Eliminar por información
    def RemoveInfo(self, delete_data):
        if self.EmptyList():
            return False
        if self.first.data == delete_data:
            self.RemoveFirst()
            return True
        PreviousNode = None
        currentNode = self.first
        while currentNode != None and currentNode.data != delete_data:
            PreviousNode = currentNode
            currentNode = currentNode.next
        if currentNode == None:
            return False
        if currentNode.next == None:
            PreviousNode.next = None
        else:
            PreviousNode.next = currentNode.next
        return True

    #Adicionar al final
    def Append(self, new_data):
        NewNode = SingleNode(new_data)
        if self.EmptyList():
            self.first = NewNode
        else:
            currentNode = self.first
            while currentNode.next != None:
                currentNode = currentNode.next
            currentNode.next = NewNode
        return NewNode
    
    #Eliminar al final
    def RemoveLast(self):
        if self.EmptyList():
            return False
        elif self.first.next == None:
            self.RemoveFirst()
            return True
        else:
            previousNode = None
            currentNode = self.first
            while currentNode.next != None:
                previousNode = currentNode
                currentNode = currentNode.next
            deleted_data = currentNode
            previousNode.next = None
            return deleted_data
        
    #Número de apariciones de un dato
    def dataCount(self, data):
        counter = 0
        if self.EmptyList():
            return False
        else:   
            currentNode = self.first
            while currentNode != None:
                if currentNode.data == data:
                    counter += 1
                currentNode = currentNode.next
            return counter
    
    #Elemento indicada una posición
    def ElementPos(self, index):
        if self.EmptyList():
            return False
        else:
            currentNode = self.first
            counter = 1
            try:
                while counter != index:
                    currentNode = currentNode.next
                    counter += 1
                return currentNode.data
            except AttributeError:
                return False
        
    #Indicar último elemento
    def LastElement(self):
        if self.EmptyList():
            return False
        else:
            currentNode = self.first
            while currentNode.next != None:
                currentNode = currentNode.next
            return currentNode.data
        
    #Eliminar elemento según posición
    def RemoveElementPos(self, index):
        if self.EmptyList():
            return False
        elif index == 1:
            self.RemoveFirst()
            return True
        else:
            previousNode = None
            currentNode = self.first
            counter = 1
            try:
                while counter != index:
                    previousNode = currentNode
                    currentNode = currentNode.next
                    counter += 1
                deleted_node = currentNode
                previousNode.next = deleted_node.next
                return deleted_node
            except AttributeError:
                return False

    #Penúltimo elemento
    def SecondLast(self):
        if self.EmptyList():
            return False
        else:
            if self.first.next == None:
                return None
            else:
                currentNode = self.first
                while currentNode.next.next != None:
                    currentNode = currentNode.next
                return currentNode
        
    #Elemento entre dos posiciones
    #def DataBetween2Pos(self, initial, final):
        if self.EmptyList():
            return False
        else:
            index = (Final - initial)








    #Eliminar todas las apariciones de un dato
    #def RemoveAlleqData(self, data):
        if self.EmptyList():
            return False
        else:
            PreviousNode = None
            currentNode = self.first
            


    #Si dos listas son iguales en longitud y contenido
    #def Comparison2Lists(self, list1, list2):
        if self.EmptyList():
            return True
        else:
            head1 = self.first
            head2 = self.first
            while head1 and head2:
                if head1.data == head2.data:
                    head1 = head1.next
                    head2 = head2.next
                else:
                    return False
            if head1 == None and head2 == None:
                return True
            else:
                return False
                   
    # Elemento de posicion inicial al final
    #def xd(self, index):
        if self.EmptyList():
            return False
        elif index == 1:
            currentNode = self.first
            while currentNode.next != None:
                currentNode = currentNode.next
            self.first.next = None
            currentNode.next = self.first
            return True
        else:
            counter = 1
            currentNode = self.first
            while currentNode.next != None:
                currentNode = currentNode.next
            x = currentNode
            previousNode = None
            currentNode = self.first
            while counter != index:
                previousNode = currentNode
                currentNode = currentNode.next
                counter += 1
            previousNode.next = currentNode.next
            currentNode.next = None
            x.next = currentNode
            return True

                
            



        


            
            

        

