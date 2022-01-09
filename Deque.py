from LinkedList import DoublyLinkedList

class Deque:
    def __init__(self):
        self.deque = DoublyLinkedList()
    
    def push_front(self,data):
        self.deque.addFirst(data)
    
    def push_back(self,data):
        self.deque.addLast(data)
    
    def pop_front(self):
        return self.deque.removeFirst()
    
    def pop_back(self):
        return self.deque.removeLast
    
    def front(self):
        return self.deque.first()
    
    def back(self):
        return self.deque.last()
    
    def isEmpty(self):
        return self.deque.isEmpty()
    
    def size(self):
        return self.deque.size()
    
    def __str__(self):
        result = ''
        current_node = self.deque.head
        while current_node != None:
            result += str(current_node.data)
            result += '\n'
            current_node = current_node.next
        return result