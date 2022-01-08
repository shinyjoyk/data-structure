class MaxPQ:
    def __init__(self,compare):
        self.compare = compare
        self.maxpq = ["dummy",None]
        self.num_of_data = 0
    
    def __less(self,i,j):
        return self.compare(self.maxpq[i],self.maxpq[j])<0
    
    def __exch(self,i,j):
        (self.maxpq[i], self.maxpq[j]) = (self.maxpq[j], self.maxpq[i])
    
    def __swim(self,k):
        while k>1 and self.__less(k//2,k):
            self.__exch(k//2,k)
            k //= 2
    
    def __sink(self,k,n):
        while 2*k < n:
            j = 2*k
            if j<n and self.__less(j,j+1):
                j+=1
            if not self.__less(k,j):
                break
            self.__exch(k,j)
            k=j
    
    def insert(self,data):
        self.num_of_data += 1
        try:
            self.maxpq[self.num_of_data] = data
        except:
            self.maxpq.append(data)
        self.__swim(self.num_of_data)
    
    def delMax(self):
        key_max = self.maxpq[1]
        self.__exch(1,self.num_of_data)
        self.num_of_data -= 1
        self.__sink(1,self.num_of_data)
        self.maxpq[self.num_of_data+1] = None
        return key_max
    
    def isEmpty(self):
        return self.num_of_data == 0
    
    def size(self):
        return self.num_of_data
    
    def max(self):
        return self.maxpq[1]
    
    def __str__(self):
        result = ''
        for i in self.maxpq[1:]:
            if i==None:
                break
            result += str(i)
            result += '\n'
        return result
    
    def sortdown(self):
        for i in range(self.num_of_data,0,-1):
            self.__exch(1,i)
            self.__sink(1,i-1)
        return self.maxpq[1:]



class MinPQ:
    def __init__(self,compare):
        self.compare = compare
        self.minpq = ["dummy",None]
        self.num_of_data = 0
    
    def __greater(self,i,j):
        return self.compare(self.minpq[i],self.minpq[j])>0
    
    def __exch(self,i,j):
        (self.minpq[i], self.minpq[j]) = (self.minpq[j], self.minpq[i])
    
    def __swim(self,k):
        while k>1 and self.__greater(k//2,k):
            self.__exch(k//2,k)
            k //= 2
    
    def __sink(self,k,n):
        while 2*k < n:
            j = 2*k
            if j<n and self.__greater(j,j+1):
                j+=1
            if not self.__greater(k,j):
                break
            self.__exch(k,j)
            k=j
    
    def insert(self,data):
        self.num_of_data += 1
        try:
            self.minpq[self.num_of_data] = data
        except:
            self.minpq.append(data)
        self.__swim(self.num_of_data)
    
    def delMin(self):
        key_min = self.minpq[1]
        self.__exch(1,self.num_of_data)
        self.num_of_data -= 1
        self.__sink(1,self.num_of_data)
        self.minpq[self.num_of_data+1] = None
        return key_min
    
    def isEmpty(self):
        return self.num_of_data == 0
    
    def size(self):
        return self.num_of_data
    
    def min(self):
        return self.minpq[1]
    
    def __str__(self):
        result = ''
        for i in self.minpq[1:]:
            if i==None:
                break
            result += str(i)
            result += '\n'
        return result
    
    def sortdown(self):
        for i in range(self.num_of_data,0,-1):
            self.__exch(1,i)
            self.__sink(1,i-1)
        return self.minpq[1:]