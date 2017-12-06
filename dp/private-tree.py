import ipdb
import time

"""
Parameters:
    w -> vector
    epsilon,delta -> privacy parameters
    t -> current round
    
"""
def private_sum(w, B, t, R, epsilon, delta, T):
    return None

def toBinary(n):
    result = ''
    if n == 0:   
        return result
    else:
        result = toBinary(n / 2)       
        return result + str(n % 2)

class Node(object):
    def __init__(self, value = -1., noiseValue = -1.):
        self.value = value
        self.noiseValue = noiseValue
        self.lchild = None
        self.rchild = None
        self.parent = None
    
    def _printTree(self, node):
        if node is not None:
            node._printTree(node.lchild)
            print str(node.value) + ' '
            node._printTree(node.rchild)

class BinaryTree(object):
    def __init__(self, root = Node(-1., -1.)):
        self.root = root
#        self.leftChild = Node(None, None)
#        self.rightChild = None
#        self.parent = None
#        self.leafCount = 0
# leaf count: use current round number t

#    def _insertLeftChild(self, parent, node):
#        if parent.lchild == None:
#            parent.lchild = node
#            node.parent = parent
#        else:
#            self._insertLeftChild(parent.lchild, node)
#
#    def insertLeftChild(self, node):
#        self._insertLeftChild(self.root, node)
#
#
#    def _insertRightChild(self, parent, node):
#        if parent.rchild == None:
#            parent.rchild = node
#            node.parent = parent
#
#    def insertRightChild(self, node):
#        self._insertRightChild(self.root, node)

    def _location(self, parent, t):
        length = len(toBinary(t))
        j = 0
        for i in toBinary(t):
            if j == length -1:
                break
            if (int(i) == 1):
                if (parent.rchild != None):
                    parent = parent.rchild
                else:
                    parent.rchild = Node()
                    parent = parent.rchild
            elif (int(i) == 0) :
                if (parent.lchild != None):
                    parent = parent.lchild
                else:
                    parent.lchild = Node()
                    parent = parent.lchild
            j += 1
        return parent,i

#    def location(self, t):
#        for i in toBinary(t):
#            self._location(self.root, i)    

    def isCompleteBT(self, t):
        if t & (t - 1) == 0:
            return True
        return False

    def _addParent(self, child, parent):
        child.parent = parent
        parent.lchild = child
        return parent

    def conRightTree(self, t, node):
        if t == 1:
            return BinaryTree(node)

#        rightTree = BinaryTree(Node())
        i = 0
        child = node
        
        while i < (len(toBinary(t))-1):
            i += 1
#            self._insertLeftChild(rightTree.root, node)
            child = self._addParent(child, Node())
        return BinaryTree(child)

    def construct(self, t, node):
        if t == 0:
            return BinaryTree(node)

#        if t == 6:
#            ipdb.set_trace()

        if self.isCompleteBT(t):
            root = Node(.0, .0)
            leftTree = self
            rightTree = self.conRightTree(t, node)
            root.lchild = leftTree.root
            leftTree.parent = root
            root.rchild = rightTree.root
            rightTree.parent = root 
            return BinaryTree(root)
        else:
            parent,i = self._location(self.root, t)    
            if int(i) == 0:
                parent.lchild = node 
            else:
                parent.rchild = node
            return self
    
    def printTree(self):
        if self.root != None:
            self.root._printTree(self.root)

if __name__ == '__main__':
    start = time.time()
    tree = BinaryTree()
    for i in range(0, 2 ** 20):
        tree = tree.construct(i, Node(i))
    end = time.time()
    print ('use %ss'%(end-start))
#    tree.printTree()

