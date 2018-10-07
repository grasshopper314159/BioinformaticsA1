# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 21:15:50 2018

@author: njayj
"""

def score(sequence1,sequence2,offset):
    return sum([1 for position in range(max(0-offset,0), min([len(sequence2)-offset, len(sequence2), len(sequence1)-offset])) if sequence2[position] == sequence1[position+offset]])

# given two sequences, find the offset which gives the best score
def find_best_offset(sequence1,sequence2):
    return max([(score(sequence1,sequence2,offset),offset,sequence2,sequence1) for offset in range(1-len(sequence2),len(sequence1))])

# given a single sequence and a collection of others, find the other sequence with the best match score
def find_best_match(sequence,others):
    return max([find_best_offset(sequence,sequence2) for sequence2 in others if sequence2 != sequence])

# given two sequences and an offset, calculate the consensus
def consensus(score,offset,sequence1,sequence2):
    return sequence2[0:max(0,offset)] + sequence1 +  sequence2[len(sequence1)+offset:]

# given a sequence and collection of others, return the complete consensus using recursion
def assemble(sequence, others):
    return consensus(*find_best_match(sequence, others)) if len(others) == 1 else assemble(consensus(*find_best_match(sequence, others)), [ y for y in others if y != find_best_match(sequence, others)[2]])

# given a collection of sequences, call assemble() to start the recursion
def assemble_helper(dnas):
    return assemble(dnas[0],dnas[1:])



#==============================================================================
if __name__=='__main__':
# =============================================================================
#     f = sys.argv[1]
#     reads = fileToArray(f)
# =============================================================================
    reads = ['TCCCAGTGAACCCA', 'TTCCGTGCGGTTAAG', 'GTCCCAGTGAACCCACAA', 'TGAACCCACAAAACG', 'ACCCACAAAACGTGA', 'GAACCCACAAAACGTGA', 'TCCGTGCGGTTAAGC', 'TGAACCCACAAA', 'CCGTGCGGTTAAGCGTGA', 'TGACAGTCCCAGTGAA', 'AACCCACAAAACGTGA', 'AGTGAACCCACAAAACGT', 'GTTAAGCGTGA', 'CCGTGCGGTTAAGCGTGA', 'AGCGTGACAGT', 'TGCGGTTAAGCG', 'ACAAAACGTGATG', 'ACAGTCCCAGTGAACC', 'TAAGCGTGACAGTCCCA', 'TCGAATTCCGT', 'TTCTCGAATTCCGTGCG', 'ACAAAACGTG', 'CCACAAAACGTG', 'TGCGGTTAAG', 'GAACCCACAAAACGTGA', 'TCTCGAATTCC', 'ATTCCGTGCGGTTAA', 'ACCCACAAAAC', 'CGTGCGGTTAAGCGTGA', 'CCAGTGAACCCACAA', 'TGCGGTTAAGCGTG', 'CCCACAAAACG', 'TCTCGAATTC', 'AATTCCGTGCGGTT', 'ACAGTCCCAGTGA', 'GTCCCAGTGAACCCA', 'TGAACCCACAAA', 'CCCACAAAACGTG', 'TCCCAGTGAACCCACA', 'CTCGAATTCCGTGCG']

    print(ah(reads))
    