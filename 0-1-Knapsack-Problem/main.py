# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 23:24:13 2020

@author: Prabal
"""
'''This is the actual knapsack function.'''
def knapSack_topDown(W, wt, val, n):
    #Create t[W+1][n+1] matrix.
    t=[[0 for x in range(W+1)] for y in range(n+1)]
    
    #Initialize "t" according to the base case.
    for i in range(n+1): #i -> n
        for j in range(W+1): #j -> W
            if i==0 or j==0:
                t[i][j]=0
    
    #Build the matrix "t" in top-down manner.
    for i in range(n+1): #i -> n
        for j in range(W+1): #j -> W
            if wt[i-1] <= j: 
                t[i][j] = max(val[i-1] + t[i-1][j-wt[i-1]], \
                                 t[i-1][j]) 
            else: 
                t[i][j] = t[i-1][j]
    return t[n][W]


'''This is the driver function with creates the input and 
all the knapsack function'''
if __name__ == '__main__':
    val = [1, 4, 5, 7] #values of the items.
    wt = [1, 3, 4, 5] #weights of the items.
    W = 7 #maximum capacity to be hold.
    n = len(val) #total number of items
    print(knapSack_topDown(W, wt, val, n))