from sortedcontainers import SortedDict

class Node(object):
    def __init__(self, val):
        self.val = val
        self.key = None
        self.children = SortedDict()
        
        
class Solution(object):
    def deleteDuplicateFolder(self, paths):
        def setKey(node):
            if not node.children:
                node.key = node.val
            else:
                node.key = ''
                for c in node.children:
                    setKey(node.children[c])
                    node.key += node.children[c].val + '|' + node.children[c].key + '|'
                
            keyCount[node.key] += 1
        
        def addPath(node, path):
            if node.children and keyCount[node.key]>1: return
            ans.append(path+[node.val])
            for c in node.children:
                addPath(node.children[c], path+[node.val])
            
            
        ans = []
        root = Node('/')
        keyCount = collections.Counter()
        
        #build the tree
        for path in paths:
            node = root
            for c in path:
                if c not in node.children: node.children[c] = Node(c)
                node = node.children[c]
        
        setKey(root)
        for c in root.children: addPath(root.children[c], [])
        return ans