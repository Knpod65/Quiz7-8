#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 12:51:49 2022

@author: kinompungpound
"""

import numpy as np

    
def CM(m):
    def CD(i,j,m):
        def IF(i,j,m):
            h=""
            if i<j and j != m:
                h+=" 0"
            elif i==j or j==m:
                h+=" 1"
            else:
                h+="-1"
            return h
        
        g=""
        if j != m:
            g+=IF(i,j,m)
            g+=". "
        else:
            g+=IF(i,j,m)
            g+="."
        return g
    
    def FR(i,m):
        z=""
        if i != m:
            for j in range(1,m+1):
                z+=CD(i,j,m)
            z+="]\n"
        else:
            for j in range(1,m+1):
                z+=CD(i,j,m)
            z+="]"
        return z
    
    c="["
    for i in range(1,m+1):
        if i ==1:
            c+="["
            c+=FR(i,m)
        else:
            c+=" ["
            c+=FR(i,m)
    c+= "]"
    return c

m=int(input("Put your order to make the square matrix (m):"))
M=np.array(CM(m))
print(M)
        