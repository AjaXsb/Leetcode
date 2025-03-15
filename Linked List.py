class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        i = 0
        current = self.head

        while current:

            if index == i:
                return current.data
                
            i += 1
            current = current.next

        return -1
        

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        exHead = self.head
        self.head = newNode
        newNode.next = exHead
        

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)

        if self.head == None:
            self.head = Node(val)

        else:
            current = self.head

            while current.next:
                current = current.next
        
            current.next = newNode
        

    def addAtIndex(self, index: int, val: int) -> None:

        if index == 0:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode
            return


        position = 0

        current = self.head

        while current and position < index - 1:
            current = current.next
            position += 1

        if current is None:
            return  
        
        newNode = Node(val)
        newNode.next = current.next
        current.next = newNode

        
        

    def deleteAtIndex(self, index: int) -> None:
        if self.head == None:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        current = self.head
        position = 0

        while current.next and position < index - 1:
            current = current.next
            position += 1

        if current.next is None:
            return False

        current.next = current.next.next

        return True
        


# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)