# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 14:10:08 2018

@author: T410 User
"""

import sys
import numpy

#==============================================================================
# def main(argv):
#   if len(argv) != 4:
#     print ('usage: <genome> <number_of_reads> <min_read_length> max_read_length>')
#     print()
#   else:
#     genome, reads, min_read_length, max_read_length = argv
#     reads, min_read_length, max_read_length = [ int(x) for x in (reads, min_read_length, max_read_length) ]
#     n = len(genome)
# 
#     for i in range(reads):
#       start = numpy.random.randint(n - min_read_length)
#       length = numpy.random.randint(min_read_length, max_read_length+1)
#       print (genome[start : start+length])
#==============================================================================

def myconcat(frags):
    s=""
    file = open(frags, 'r')
    for line in file.readlines():
        s = s+line.strip()
    file.close()
    return s

def fileToList(frags):
    s=""
    file = open(frags, 'r')
    for line in file.readlines():
        s = s+line
    file.close()
    return s

def multipleOfK(n,k):
    if n%k == 0: 
        return n
    return n + (k- (n%k))
    

def kmers(s,k):
    mers = []
    #listSize = int(multipleOfK(len(s),k)/k)
    listSize = len(s) - (k-1)
    print("listsize= ", listSize)
    print("length = ", len(s))
    for i in range(listSize):
       mers.append(s[:k])
       s = s[1:]
    return mers
    

#==============================================================================
#     for line in frags:
#         s = s+line
#     return s
#==============================================================================


#==============================================================================
# if __name__=='__main__':
#   main(sys.argv[1:])
#==============================================================================
if __name__=='__main__':
    f = sys.argv[1]
    s2=myconcat(sys.argv[1])
    print(s2)
    kmers('KIHOIHOI',3)
    print(multipleOfK(3,3))
    print(multipleOfK(4,3))
    print(multipleOfK(5,3))
    mers=kmers(s2,5)
    mers.sort()
    print (mers)
    print(fileToList(f))