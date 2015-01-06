
"""
Created on Fri Oct 10 20:15:20 2014

@author: Iliass Tiendrebeogo
machine epsilon """

""" Dscription: Mimic the machine epsilon """
epsilon = 1.0
p = 0
while 1.0 != 1.0 + epsilon:
    
    epsilon = epsilon/2.0 # divide until epsilon become not distinctive to zero
    print p,'................', epsilon
    p = 1+p
print 'final eps:', epsilon
print 'p is:', p
