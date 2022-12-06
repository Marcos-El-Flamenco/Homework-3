class Node:


    def __init__(self,i):
        self.indentifier = i
        self.parent = self
        self.classSize = 1

    def get_class(self):
        if self == self.parent:
            return self
        else:
            big_daddy = self.parent.get_class()
            self.parent = big_daddy
            return big_daddy


class DisjointSet:

    def __init__(self):
        self.forest = []

    def addSet(self,i):
        node = Node(i)
        self.forest.append(node)
        return node

    def union(self,a,b):
        if (a.get_class() == b.get_class()):
            pass
        else:
            asize = a.classSize
            bsize = b.classSize
            if (asize >= bsize):
                b.parent = a
                self.forest.remove(b)
            else:
                a.parent = b
                self.forest.remove(a)
            b.classSize = asize + bsize
            a.classSize = asize + bsize
                







def friend_groups(M):
    n = len(M)
    set = DisjointSet()
    nodes = [set.addSet(i) for i in range(n)]
    for i in range(n):
        for j in range(i):
            if M[i][j]:
                set.union(nodes[i],nodes[j])

    return len(set.forest)


M = [[1,1,0,0],
     [1,1,1,0],
     [0,1,1,0],
     [0,0,0,1]]
print(friend_groups(M))
