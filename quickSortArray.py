# -*- coding: utf-8 -*-
"""
Created on Tue May  7 00:05:06 2019

@author: Jahnavi Jaddi
"""

import numpy as np
#from numpy import median
import array

def quickSort(list1,pivot_index,pivot,leng):
    small_list,large_list,equallist=[],[],[]
    for i in range(0,leng):
        if list1[i]<pivot:
            small_list.append(list1[i])
        elif list1[i]>pivot:
            large_list.append(list1[i])
        elif list1[i]==pivot:
            equallist.append(list1[i])
    sortlist(small_list,len(small_list))
    sortlist(large_list,len(large_list))
    list2=small_list+equallist+large_list
    return list2
     
def sortlist(lists,leng):
    count=0
    for i in range(0,leng-1):
        if lists[i]>lists[i+1]:
            a=lists[i+1]
            lists[i+1]=lists[i]
            lists[i]=a
            sortlist(lists,leng)
        else:
            count+=1
            if count==leng:
                break
            



if __name__=="__main__":
    #list1=[10,9,8,7,6,5,4,3,2]
    
    raw_list= input("input the array elements in a line: ").split(" ")
    list1=[int(i) for i in raw_list]
    leng=len(list1)
    mid=int(((leng-1)/20))
    median1=int(np.median(list1))#int(median([int(list1[0]),int(list1[mid]),int(list1[len(list1)-1])]))
    print("median is ", median1)
    pivot_index=list1.index(median1)
    print(str(list1))
    b=list1[pivot_index]
    count=0
    print("Before sorting:  ",str(list1))
    list2=str(quickSort(list1,pivot_index,b,leng))
    print("after sorting ",str(list2))
