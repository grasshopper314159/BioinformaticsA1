# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 23:26:10 2018

@author: njayj
"""
import copy
import string
import random
from itertools import product
from collections import defaultdict

import numpy as np

random.seed(123)
np.random.seed(321)

genome = "".join(random.choice("AGCT") for _ in range(1000))

def perfect_reads(genome, n_reads=10):
    """Create perfect reads from `genome`"""
    starts = np.random.randint(len(genome), size=n_reads)
    length = np.random.randint(27,33, size=n_reads)
    for n in range(n_reads):
        low = starts[n]
        yield genome[low:low + length[n]]
        
def kmers(read, k=10):
    """Generate `k`-mers from a `read`"""
    for n in range(len(read) - k + 1):
        yield read[n:n+k]
        
def get_perfect_kmers(genome):
    kmers_ = []
    for read in perfect_reads(genome, n_reads=1000):
        for kmer in kmers(read):
            kmers_.append(kmer)
            
    return kmers_

kmers_ = get_perfect_kmers(genome)
# lots of kmers, but not that many are unique
print(len(kmers_), len(set(kmers_)))

#from graphviz import Digraph
def make_graph(string, k):
    k_mers = list(kmers(string, k))
    nodes = defaultdict(list)

    for kmer in k_mers:
        head = kmer[:-1]
        tail = kmer[1:]
        nodes[head].append(tail)
        
    return nodes

nodes = make_graph('abcbdexdbfga', 2)
print(nodes)

def edges(graph):
    """List all directed edges of `graph`"""
    for node in graph:
        for target in graph[node]:
            yield (node, target)


def follow_tour(tour, graph):
    """Follow a tour and check it is eulerian"""
    edges_ = list(edges(graph))
    for start, end in zip(tour, tour[1:]):
        try:
            edges_.remove((start, end))
        # most likely removing an edge that was already used
        except:
            return False
        
    # if there are any edges left this is neither
    # an eulerian tour nor an eulerian trail
    if edges_:
        return False
    else:
        return True


def check_tour(start, graph):
    our_tour = tour(start, graph)
    valid_tour = follow_tour(our_tour, graph)
    return valid_tour, "".join(s[0] for s in our_tour)

def tour(start_node, graph):
    """Find an eulerian cycle or trail.
    
    This does not check if the graph is eulerian
    so it might return tours that are nonsense.
    """
    # _tour() modifies the graph structure so we need to copy it
    graph = copy.deepcopy(graph)
    return _tour(start_node, graph)

def _tour(start_node, graph, end=None):
    tour = [start_node]
    finish_on = end if end is not None else start_node
    while True:
        options = graph[tour[-1]]

        # eulerian trail, not tour?
        if not options:
            break
        
        tour.append(options.pop())
        if tour[-1] == finish_on:
            break
    
    # when we insert a sub-tour we extend the
    # length of tour, need to track this
    offset = 0
    for n,step in enumerate(tour[:]):
        options = graph[step]
        if options:
            t = _tour(options.pop(), graph, step)
            n += offset
            tour = tour[:n+1] + t + tour[n+1:]
            offset += len(t)
            
    return tour

