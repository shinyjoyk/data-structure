from LinkedList import SinglyLinkedList

class Stack:
    def __init__(self):
        self.stack = SinglyLinkedList()
    
    def push(self,data):
        self.stack.addFirst(data)
    
    def pop(self):
        return self.stack.removeFirst()
    
    def top(self):
        return self.stack.first()
    
    def isEmpty(self):
        return self.stack.isEmpty()
    
    def size(self):
        return self.stack.size()
    
    def __str__(self):
        result = ''
        current_node = self.stack.head
        while current_node != None:
            result += str(current_node.data)
            result += '\n'
            current_node = current_node.next
        return result