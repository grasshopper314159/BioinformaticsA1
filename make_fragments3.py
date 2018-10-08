# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
import numpy

def make_f(path_to_genome_excerpt,reads,min_read_length,max_read_length):
  write_path = "natesFrags.txt"

# =============================================================================
#   if len(argv) != 4:
#     print ('usage: <genome> <number_of_reads> <min_read_length> max_read_length>')
#     print()
# =============================================================================
  try:
      with open(path_to_genome_excerpt,'r') as f:
        genome = f.read()
        reads, min_read_length, max_read_length = [ int(x) for x in (reads, min_read_length, max_read_length) ]
        n = len(genome)
  except:
    print('Error opening genome file')
  l=[]  
  with open(write_path,'w') as f:
    for i in range(reads):
      start = numpy.random.randint(n - min_read_length)
      length = numpy.random.randint(min_read_length, max_read_length+1)
      l.append((genome[start : start+length]+'\n'))
      #print (genome[start : start+length])
  print('Length of genome is: ',n)
  print('Reads: ',reads)
  return l
  

# =============================================================================
# if __name__=='__main__':
#   make_f(sys.argv[1:])
# =============================================================================
