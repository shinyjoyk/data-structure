class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.priv = None

class DoublyLinkedList:
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
            self.head.priv = new_node
            self.head = new_node
        self.num_of_data += 1
    
    def addLast(self,data):
        new_node = Node(data)
        if self.size() == 0:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.priv = self.tail
            self.tail = new_node
        self.num_of_data += 1
    
    def removeFirst(self):
        if self.isEmpty():
            return -1
        elif self.size() == 1:
            result = self.first()
            dummy = Node("dummy")
            self.head = dummy
            self.tail = dummy
            self.num_of_data = 0
        else:
            result = self.first()
            self.head = self.head.next
            self.head.priv = None
            self.num_of_data -= 1
        return result
    
    def removeLast(self):
        if self.isEmpty():
            return -1
        elif self.size() == 1:
            result = self.last()
            dummy = Node("dummy")
            self.head = dummy
            self.tail = dummy
            self.num_of_data = 0
        else:
            result = self.last()
            self.tail = self.tail.priv
            self.tail.next = None
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
        return self.deque.removeLast()
    
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

import sys

deque = Deque()

for _ in range(int(sys.stdin.readline().strip())):
    command = sys.stdin.readline().strip()
    if 'push_front' in command:
        deque.push_front(int(command[10:]))
    elif 'push_back' in command:
        deque.push_back(int(command[9:]))
    elif command == 'pop_front':
        print(deque.pop_front())
    elif command == 'pop_back':
        print(deque.pop_back())
    elif command == 'size':
        print(deque.size())
    elif command == 'empty':
        print(1 if deque.isEmpty() else 0)
    elif command == 'front':
        print(deque.front())
    elif command == 'back':
        print(deque.back())
    else:
        print('command error')