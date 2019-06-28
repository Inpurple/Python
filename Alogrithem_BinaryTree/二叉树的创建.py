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
        if not self.root:
            self.root=Node(item)# 传入node类型的数据
            return
        else:
            queue=[self.root]
            while queue:
                curnode=queue.pop(0)
                if curnode.left==None:
                    self.left=curnode
                    return
                else:
                    queue.append(self.left)#队列里加的是当前节点的左子节点，而不是新节点
                if curnode.right==None:
                    
                    self.right=curnode
                    return
                else:
                    queue.append(self.right)
                    
    

                
        
