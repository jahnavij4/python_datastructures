# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:25:59 2019

@author: jahnavi
"""
import array
def Arraysort(array1,num):
    mid= int((len(array1)-1)/2)
    #print(mid)
    index=0
    if num<=mid:
        for i in range(0, mid):
            if int(array1[i])==int(num):
                index=i
                
    if num>=mid:
        for i in range(mid, (len(array1)-1)):
            if int(array1[i])==num:
                index=i
    return index
    

    
if __name__=="__main__":
    list1=input("array elements : ").split(" ")
    print(list1)
    num=int(input())
    position=Arraysort(list1, num) 
    print ("The position of the element {0} in the input sorted array is {1}".format(num,position))
