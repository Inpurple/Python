# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Node(object):
    
    def __init__(self,item):
        self.value=item
        self.left=None
        self.right=None
        
        
class BinaryTree(object):
    def __init__(self):
        self.root=None
    
    def add(self,item):
        node=Node(item)
        if not self.root:
            self.root=node# 传入node类型的数据
            return
        else:
            queue=[self.root]
            while queue:
                curnode=queue.pop(0)
                if curnode.left is None:
                    curnode.left=node
                    return
                else:
                    queue.append(curnode.left)#队列里加的是当前节点的左子节点，而不是新节点
                if curnode.right is None:
                    
                    curnode.right=node
                    return
                else:
                    queue.append(curnode.right)
                    
    def breadth_travelsal(self):
        if not self.root:
            return
        else:
            queue=[self.root]
            while queue:
                curnode=queue.pop(0)
                print(curnode.value)
                if curnode.left!=None:
                    queue.append(curnode.left)
                if curnode.right!=None:
                    queue.append(curnode.right)
if __name__=="__main__":
    
    tree=BinaryTree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.breadth_travelsal()
                    
        
