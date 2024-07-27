# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 09:42:40 2023

@author: asala
"""
def merge(A, p, q, r):         # defining merge function
    temp = []                                 # initializing empty temp list
    i = p
    j = q
    while i < q and j < r:
        if A[i] < A[j]:           # checking if the left sublist has the lower element
            temp.append(A[i])
            i += 1
        else:                                 
            temp.append(A[j])
            j += 1
    while i < q:                            # filling the list with remainders of the left sublist
        temp.append(A[i])
        i += 1
    while j < r:                          # filling the list with remainders of the right sublist
        temp.append(A[j])
        j += 1
    for k in range(p, r):              # setting the values of the temp list to the main list
        A[k] = temp[k - p]
 
def BottomUpMergeSortAlgorithm(A,p,r):
     n=len(A)
     t = 1
     while t < n:
         s = t 
         t = 2*s 
         i = 0
         while i + t <= n:
             merge(A, i , i + s, i + t)
             i = i + t
         if i + s < n :
             merge(A, i + 1, i+ s, n)    
  
