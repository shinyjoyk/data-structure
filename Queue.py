from LinkedList import SinglyLinkedList

class Queue:
    def __init__(self):
        self.queue = SinglyLinkedList()
    
    def enqueue(self,data):
        self.queue.addLast(data)
    
    def dequeue(self):
        return self.queue.removeFirst()
    
    def first(self):
        return self.queue.first()
    
    def isEmpty(self):
        return self.queue.isEmpty()
    
    def size(self):
        return self.queue.size()
    
    def __str__(self):
        result = ''
        current_node = self.queue.head
        while current_node != None:
            result += str(current_node.data)
            result += '\n'
            current_node = current_node.next
        return result