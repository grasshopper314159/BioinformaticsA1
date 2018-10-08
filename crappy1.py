# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 21:17:32 2018

@author: njayj
"""
# =============================================================================
# 
# score() is the basic scoring function. It takes two sequences and an offset, and returns the number of characters 
# that match. It's the simplest possible function for scoring an ungapped alignment between two sequences. 
# It works by calculating the first and last positions of the overlapping region relative to sequence2,
#  then counts up the number of positions for which the base in sequence2 is the same as the base in 
#  sequence1 at that position plus the offset. To get everything in one expression, it uses 
#a list comprehension to build a list of 1's for each matching position, then sums the list.
# Here it is written out a bit more conventionally. The only complicated thing going on here is the
# calculation of the start and stop positions.
# 
# =============================================================================
def score(sequence1,sequence2,offset):
    start_of_overlap = max(0-offset,0)
    end_of_overlap = min([len(sequence2)-offset, len(sequence2), len(sequence1)-offset])
    total_score = 0
    for position in range(start_of_overlap, end_of_overlap):
        if sequence2[position] == sequence1[position+offset]:
            total_score = total_score + 1
    return total_score
#find_best_offset() is the function that tries to maximize the score for a pair of sequences

def find_best_offset(sequence1,sequence2):
    lowest_offset = 1-len(sequence2)
    highest_offset = len(sequence1)
    all_offsets = []
    for offset in range(lowest_offset,highest_offset):
        # add the 4-tuple for this offset
        all_offsets.append((score(sequence1,sequence2,offset),offset,sequence2,sequence1))
    return max(all_offsets)
#find_best_match() is probably the most straightforward function of the bunch. Given a single sequence and a list of other sequences, it finds the other sequence that has the best match by calling find_best_offset() for each of them in turn. It uses the same tuple-sorting trick as before to figure out which match is the best:

def find_best_match(sequence,others):
    all_matches = []
    for sequence2 in others:
        if sequence2 != sequence:
            all_matches.append(find_best_offset(sequence,sequence2))
    return max(all_matches)
#The consensus() function gave me quite a bit of trouble. Its job is to take two sequences plus a given offset, and return the consensus sequence of the two. Of course, it doesn't do anything like what we normally mean by consensus – it simply concatenates the relevant bits of the two sequences to make a longer one. The logic behind how it works is a little bit hard to follow. We construct the consensus sequence by taking the full length of sequence1, and sticking any left-hand overhang from sequence2 on the left end and any right-hand overhang from sequence2 on the right end. In other words, you should read the return line as "return any bits of sequence2 that stick out to the left, followed by the whole of sequence1, followed by any bits of sequence2 that stick out to the right". For most overlapping pairs of sequences, either the first or last bit of the returned string will be zero-length, which is why the thing works as a single expression in the compact version.

def consensus(score,offset,sequence1,sequence2):
    sequence2_left_overhang = sequence2[0:max(0,offset)]
    sequence2_right_overhang = sequence2[len(sequence1)+offset:]
    return sequence2_left_overhang + sequence1 + sequence2_right_overhang
#The assemble() function is probably the most complicated (and certainly the most inefficient). 
#I cheated a little bit to get it onto a single line by using the ternary operator x if y else z. 
#It's a recursive function that takes a single sequence and a collection of other sequences. 
#It finds the best match for the sequence among the others and calculates the consensus
# of the sequence and the best-matching other. If that's the only member of others
# (i.e. the others list has just one element) it simply returns the consensus. If the others 
#list has more than one element, it removes the best matching one and calls itself recursively with
# the newly built consensus as the single sequence. Here it is expanded:

def assemble(sequence, others):
    # remember, best_matching_other is a 4-tuple
    best_matching_other = find_best_match(sequence, others)
    # the * expands the elements of the tuple so we can use them as arguments to consensus()
    consensus_sequence = consensus(*best_matching_other)
    if len(others) == 1:
        return consensus_sequence
    else:
        # get the second element of the best_matching_other tuple, which is the sequence
        best_matching_sequence = best_matching_other[2]
        others.remove(best_matching_sequence)
        return assemble(consensus_sequence, others)
    
    # given a collection of sequences, call assemble() to start the recursion
def assemble_helper(dnas):
    return assemble(dnas[0],dnas[1:])

def ah(d):
    return assemble(d[0],d[1:])

#%%
def fileToList(frags):
    s=""
    file = open(frags, 'r')
    for line in file.readlines():
        s = s+line
        print(line)
    file.close()
    return s

#%%
def fileToArray(frags):
    s=[]
    file = open(frags, 'r')
    for line in file.readlines():
        s.append(line.strip())
    file.close()
    return s
#%%
import sys, numpy
#==============================================================================
# =============================================================================
# if __name__=='__main__':
#     f = sys.argv[1]
#     
#     
#     reads = fileToArray(f)
# #    reads = ['TCCCAGTGAACCCA', 'TTCCGTGCGGTTAAG', 'GTCCCAGTGAACCCACAA', 'TGAACCCACAAAACG', 'ACCCACAAAACGTGA', 'GAACCCACAAAACGTGA', 'TCCGTGCGGTTAAGC', 'TGAACCCACAAA', 'CCGTGCGGTTAAGCGTGA', 'TGACAGTCCCAGTGAA', 'AACCCACAAAACGTGA', 'AGTGAACCCACAAAACGT', 'GTTAAGCGTGA', 'CCGTGCGGTTAAGCGTGA', 'AGCGTGACAGT', 'TGCGGTTAAGCG', 'ACAAAACGTGATG', 'ACAGTCCCAGTGAACC', 'TAAGCGTGACAGTCCCA', 'TCGAATTCCGT', 'TTCTCGAATTCCGTGCG', 'ACAAAACGTG', 'CCACAAAACGTG', 'TGCGGTTAAG', 'GAACCCACAAAACGTGA', 'TCTCGAATTCC', 'ATTCCGTGCGGTTAA', 'ACCCACAAAAC', 'CGTGCGGTTAAGCGTGA', 'CCAGTGAACCCACAA', 'TGCGGTTAAGCGTG', 'CCCACAAAACG', 'TCTCGAATTC', 'AATTCCGTGCGGTT', 'ACAGTCCCAGTGA', 'GTCCCAGTGAACCCA', 'TGAACCCACAAA', 'CCCACAAAACGTG', 'TCCCAGTGAACCCACA', 'CTCGAATTCCGTGCG']
# 
#     print(ah(reads))
# =============================================================================
    
if __name__=='__main__':
    f = sys.argv[1]
    
    
    reads = fileToArray(f)
#    reads = ['TCCCAGTGAACCCA', 'TTCCGTGCGGTTAAG', 'GTCCCAGTGAACCCACAA', 'TGAACCCACAAAACG', 'ACCCACAAAACGTGA', 'GAACCCACAAAACGTGA', 'TCCGTGCGGTTAAGC', 'TGAACCCACAAA', 'CCGTGCGGTTAAGCGTGA', 'TGACAGTCCCAGTGAA', 'AACCCACAAAACGTGA', 'AGTGAACCCACAAAACGT', 'GTTAAGCGTGA', 'CCGTGCGGTTAAGCGTGA', 'AGCGTGACAGT', 'TGCGGTTAAGCG', 'ACAAAACGTGATG', 'ACAGTCCCAGTGAACC', 'TAAGCGTGACAGTCCCA', 'TCGAATTCCGT', 'TTCTCGAATTCCGTGCG', 'ACAAAACGTG', 'CCACAAAACGTG', 'TGCGGTTAAG', 'GAACCCACAAAACGTGA', 'TCTCGAATTCC', 'ATTCCGTGCGGTTAA', 'ACCCACAAAAC', 'CGTGCGGTTAAGCGTGA', 'CCAGTGAACCCACAA', 'TGCGGTTAAGCGTG', 'CCCACAAAACG', 'TCTCGAATTC', 'AATTCCGTGCGGTT', 'ACAGTCCCAGTGA', 'GTCCCAGTGAACCCA', 'TGAACCCACAAA', 'CCCACAAAACGTG', 'TCCCAGTGAACCCACA', 'CTCGAATTCCGTGCG']

    print(ah(reads))