from typing import List

def log(*args):
    # print(args)
    pass

class Node:
    def __init__(self):
        self.val = None
        # self.leafs = []
        self.zero = None
        self.one = None

    def insert(self, node, bit):
        # log('insert, bit=', bit, 'leaf=', leaf)
        # self.leafs.append(leaf)
        if bit == 0:
            if self.zero == None:
                self.zero = node
            return self.zero
        else:
            if self.one == None:
                self.one = node
            return self.one
    
    def set_val(self, val):
        self.val = val

    def get(self, bit):
        if bit == 0:
            return self.zero
        else:
            return self.one
        
    def printAll(self, deep=0):
        # print('deep', deep, 'leafs', self.leafs)
        if self.zero != None:
            print('zero')
            self.zero.printAll(deep+1)
        if self.one != None:
            print('one')
            self.one.printAll(deep+1)
        if self.val != None:
            print('val: ', self.val)

    def get_max_xor(self, bit):
        if bit == 0:
            if self.one:
                # print('get_max_xor 1', self.val)
                return self.one
            else:
                # print('get_max_xor 2', self.val)
                return self.zero
        else:
            if self.zero:
                # print('get_max_xor 3', self.val)
                return self.zero
            else:
                # print('get_max_xor 4', self.val)
                return self.one

    def get_val(self):
        return self.val


def get_max_xor(numbers: List[int]) -> int:
    r = 0

    if len(numbers) < 2:
        return 0

    i = 0x80000000
    while i > 0:

        len1 = 0
        len2 = 0
        for n in numbers:
            if n & i > 0:
                len1 += 1
            else:
                len2 += 1

        # print(i, arr1, arr2)
        if len1 > 0 and len2 > 0:

            arr1 = []
            arr2 = []
            for n in numbers:
                if n & i > 0:
                    arr1.append(n)
                else:
                    arr2.append(n)
            
            tree = Node()
            for n2 in arr2:
                it = tree
                # print('arr2: ', n2)
                j = i >> 1
                while j > 0:
                    # print('j=', j)
                    it = it.insert(Node(), j & n2)
                    j = j >> 1
                it.set_val(n2)

            # tree.printAll()
            for n1 in arr1:
                j = i >> 1
                it = tree

                # print(j, len(it[0]), len(it[1]))
                while j > 0:
                    # print(n1 & j)
                    it = it.get_max_xor(n1 & j)
                    j = j >> 1
                # print('n1', n1, 'it.get_val()', it.get_val(), r, n1 ^ it.get_val())
                r = max(r, n1 ^ it.get_val())
            break

        i = i >> 1
    return r

n = int(input())
numbers = list(map(int, input().split()))
print(get_max_xor(numbers))