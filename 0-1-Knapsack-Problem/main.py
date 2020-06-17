# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 23:24:13 2020

@author: Prabal
"""
'''This is the actual knapsack function.'''
def knapSack(W, wt, val, n):
    return


'''This is the driver function with creates the input and 
all the knapsack function'''
if __name__ == '__main__':
    val = [60, 100, 120] #values of the items.
    wt = [10, 20, 30] #weights of the items.
    W = 50 #maximum capacity to be hold.
    n = len(val) #total number of items
    print(knapSack(W, wt, val, n))