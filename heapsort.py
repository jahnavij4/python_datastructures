# -*- coding: utf-8 -*-
"""
Created on Tue May  7 17:10:53 2019

@author: Jahnavi Jaddi
"""
def heapsort(list1,index,n):
    large=index
    rindex=2*index+2
    lindex=2*index+1
    
    if rindex < n and list1[rindex]>list1[index]:
        large=rindex
        
    if lindex < n and list1[lindex]>list1[large]:
        large=lindex
        
    if large !=index:
        list1[index],list1[large]=list1[large],list1[index]
        heapsort(list1,large,n)
                
    return list1

if __name__=="__main__":
    raw_list=input("provide the array to be sorted: ").split(" ")
    list1=[int(i) for i in raw_list]
    #list1=[12,35,87,26,9,28,7]
    n=len(list1)
    list2=[]
    for x in range(n-1,-1,-1):
        list2=heapsort(list1,x,n)
    print("max heapsorted list is: ",list2)
    
    for y in range(n-1,0,-1):
        #print(n-y," ",y-1)
        list2[0],list2[y]=list2[y],list2[0]
        list2=heapsort(list2,0,y)
    print("sorted heapsorted list is: ",list2)
        