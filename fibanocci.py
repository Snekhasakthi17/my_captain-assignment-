# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 19:13:32 2022

@author: EDITMEDIA
"""

nterms=int(input("how many terms?"))
n1,n2=0,1
count=0
if nterms<=0:
    print("enter a positive integer")
elif nterms==1:
    print("fibanacci sequence upto",nterms,":")
    print(n1)
else:
    print("fibanocci sequence:")
    while count < nterms:
        print(n1)
        nth=n1+n2
        n1 = n2
        n2 = nth
        count+=1
              