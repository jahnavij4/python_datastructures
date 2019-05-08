# -*- coding: utf-8 -*-
"""
Created on Tue May  7 20:35:58 2019

@author: Jahnavi Jaddi
"""

def sort(list1):
    
    for x in range(0,len(list1)-1):
        if list1[x]>list1[x+1]:
            a=list1[x]
            list1[x]=list1[x+1]
            list1[x+1]=a
            sort(list1)
    return list1


def finalsort(list11,list12):
    p,q=0,0
    finallist=[]
    len1=len(list11)
    len2=len(list12)
    #print(len1, len2)
    while p<len1 and q<len2:
            
            if list12[q]<list11[p]:
                 finallist.append(list12[q])
                 #print(finallist)
                 q+=1
            else:
                 finallist.append(list11[p])
                 #print(finallist)
                 p+=1
    print(p)    
    while p< len1:
        finallist.append(list11[p])
        p+=1
    while q<len2:
        finallist.append(list12[q])
        q+=1
    return finallist
    

if __name__=="__main__":
    raw_list=input("provide the array elements in single line: ").split(" ")
    list1=[int(i) for i in raw_list]
#    list1=[12,35,87,26,9,28,7]
    mid=int(len(list1)/2)
    list11=sort(list1[:mid])
    list12=sort(list1[mid:])
    print("given list: ",list1, "1st half ",list11," second half ",list12)
    print("final merge sorted list is : ",finalsort(list11,list12))