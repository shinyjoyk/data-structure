class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        dummy = Node("dummy")
        self.head = dummy
        self.tail = dummy
        
        self.num_of_data = 0
    
    def size(self):
        return self.num_of_data
    
    def isEmpty(self):
        return self.num_of_data == 0
    
    def first(self):
        if self.isEmpty():return -1
        return self.head.data
    
    def last(self):
        if self.isEmpty():return -1
        return self.tail.data
    
    def addFirst(self,data):
        new_node = Node(data)
        if self.size() == 0:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_of_data += 1
    
    def addLast(self,data):
        new_node = Node(data)
        if self.size() == 0:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.num_of_data += 1
    
    def removeFirst(self):
        if self.isEmpty():
            return -1
        else:
            result = self.first()
            self.head = self.head.next
            self.num_of_data -= 1
        return result
    
    def removeLast(self):
        if self.isEmpty():
            return -1
        elif self.size() ==1:
            result = self.last()
            self.num_of_data -= 1
            self.head = Node("dummy")
            self.tail = Node("dummy")
        else:
            result = self.last()
            current_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next
            current_node.next = None
            self.tail = current_node
            self.num_of_data -= 1
        return result
    
    def __str__(self):
        result = ''
        current_node = self.head
        while current_node != None:
            result += str(current_node.data)
            result += '\n'
            current_node = current_node.next
        return result


class CircularlyLinkedList:
    def __init__(self):
        dummy = Node("dummy")
        self.tail = dummy
        
        self.num_of_data = 0
    
    def size(self):
        return self.num_of_data
    
    def isEmpty(self):
        return self.num_of_data == 0
    
    def first(self):
        return self.tail.next.data
    
    def last(self):
        return self.tail.data
    
    def rotate(self):
        if self.tail.next != None:
            self.tail= self.tail.next
    
    def addFirst(self,data):
        new_node = Node(data)
        if self.isEmpty():
            self.tail = new_node
            self.tail.next = self.tail
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
        self.num_of_data += 1
    
    def addLast(self,data):
        self.addFirst(data)
        self.rotate()
    
    def removeFirst(self):
        result = self.first()
        if not self.isEmpty():
            if self.size() == 1:
                self.tail.next = Node("dummy")
            else:
                self.tail.next = self.tail.next.next
            self.num_of_data -= 1
        return result
    
    def __str__(self):
        result = ''
        current_node = self.tail.next
        while current_node != self.tail:
            result += str(current_node.data)
            result += '\n'
            current_node = current_node.next
        result += str(current_node.data)
        return result+"\n"
