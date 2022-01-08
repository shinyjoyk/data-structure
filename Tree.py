class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self,compare):
        self.compare = compare
        self.root = None
        self.num_of_data = 0
    
    def search(self,data):
        current_node = self.root
        while current_node!=None:
            if current_node.data == data:
                return True
            elif self.compare(data,current_node.data) > 0:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return False
    
    def insert(self,data):
        if self.isEmpty():
            self.root = Node(data)
        else:
            current_node = self.root
            while True:
                if self.compare(data,current_node.data) > 0:
                    if current_node.right == None:
                        current_node.right = Node(data)
                        break
                    current_node = current_node.right
                else:
                    if current_node.left == None:
                        current_node.left = Node(data)
                        break
                    current_node = current_node.left
        self.num_of_data += 1
    
    def inorder(self):
        if self.isEmpty():
            return ''
        else:
            return self._inorder_node(self.root).replace("\n\n","\n")
    
    def _inorder_node(self,node):
        if node == None:
            return ''
        if node.left == None and node.right == None:
            return str(node.data)+'\n'
        return self._inorder_node(node.left)+"\n"+str(node.data)+"\n"+self._inorder_node(node.right)
    
    def preorder(self):
        if self.isEmpty():
            return ''
        else:
            return self._preorder_node(self.root).replace("\n\n","\n")
    
    def _preorder_node(self,node):
        if node == None:
            return ''
        if node.left == None and node.right == None:
            return str(node.data)+'\n'
        return str(node.data)+"\n"+self._preorder_node(node.left)+"\n"+self._preorder_node(node.right)
    
    def postorder(self):
        if self.isEmpty():
            return ''
        else:
            return self._postorder_node(self.root).replace("\n\n","\n")
    
    def _postorder_node(self,node):
        if node == None:
            return ''
        if node.left == None and node.right == None:
            return str(node.data)+'\n'
        return self._postorder_node(node.left)+"\n"+self._postorder_node(node.right)+"\n"+str(node.data)
    
    def getSize(self):
        return self.num_of_data
    
    def isEmpty(self):
        return self.num_of_data == 0
    
    def height(self):
        return self._height(self.root)
    
    def _height(self,node):
        if node == None:
            return -1
        if node.left == None and node.right == None:
            return 0
        return max(self._height(node.left),self._height(node.right))+1
    
    def min(self):
        return self._min(self.root).data
    
    def _min(self,node):
        if node == None:
            return None
        elif node.left == None:
            return node
        else: return self._min(node.left)
    
    def deleteMin(self):
        if not self.isEmpty():
            self.root = self._deleteMin(self.root)
            self.num_of_data -= 1
    
    def _deleteMin(self,node):
        if node.left == None: return node.right
        node.left = self._deleteMin(node.left)
        return node
    
    
    def delete(self,data):
        if not self.isEmpty():
            self.root = self._delete(self.root,data)
            self.num_of_data -= 1
    
    def _delete(self,node,data):
        if node == None: return None
        cmp = self.compare(data,node.data)
        if cmp < 0: node.left = self._delete(node.left,data)
        elif cmp > 0: node.right = self._delete(node.right,data)
        else:
            if node.right == None: return node.left
            if node.left == None: return node.right
            node_1 = self._min(node.right)
            node_1.right = self._deleteMin(node.right)
            node_1.left = node.left
            return node_1
        return node