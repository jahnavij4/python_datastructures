# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:05:48 2019

@author: Jahnavi Jaddi
"""
import queue
class bfsSearch():
    def __init__(self, gdict=None):
        if gdict==None:
            gdict={}
        self.gdict=gdict
#
#def search(self,node):
#    explored=[]
#    queue=[node]
#     
#    while queue:
#         node1=queue.pop(0)
#         if node not in explored:
#             explored.append(node1)
#             neighbours=graph_elements[node1]
#             for neighbour in neighbours:
#                 queue.append(neighbour)
#                
#    return explored

def shortestPath(graph,start, goal):
    explored=[]
    
    queue1=[[start]]
    
    if start==goal:
        return "start and goal are same"
    
    while queue1:
#        print("before queue is ",queue1)
        path=queue1.pop(0)
        node=path[-1]
#        print ("path is ",path)
#        print("after pop queue is ",queue1)
#        print("node is ",node)
#        print ("---------------------------------------------")
#        
        if node not in explored:
            neighbours=graph[node]
            #print(graph[node])
            for neighbour in neighbours:
                new_path=list(path)
                new_path.append(neighbour)
                queue1.append(new_path)
                if neighbour==goal:
                    return new_path
                
            explored.append(node)
    return "checking"


graph_elements = { "a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d","f"],
                "d" : ["e"],
                "e" : ["d"],
                "f" : ["c","e"]
                }  
g=bfsSearch(graph_elements)   
#print (search(g.gdict,'a'))
print (shortestPath(g.gdict,'a','d'))