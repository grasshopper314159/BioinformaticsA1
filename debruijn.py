# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 21:07:29 2018

@author: njayj
"""
#TAATGCCATGGGATGTT
def debruijn(str, k):
    edges = []
    nodes = set()
    for i in range(len(str)-k+1):
        edges.append((str[i:i+k-1], str[i+1:i+k]))
        nodes.add(str[i:i+k-1])
        nodes.add(str[i+1:i+k])
    return nodes, edges

#nodes, edges = debruijn("ACGCGTCG", 3)

# =============================================================================
# def visualize_de_bruijn(st, k):
#     """ Visualize a directed multigraph using graphviz """
#     nodes, edges = debruijn(st, k)
#     dot_str = 'digraph "DeBruijn graph" {\n'
#     for node in nodes:
#         dot_str += '  %s [label="%s"] ;\n' % (node, node)
#     for src, dst in edges:
#         dot_str += '  %s -> %s ;\n' % (src, dst)
#     return dot_str + '}\n'
# =============================================================================

def visualize_de_bruijn(st, k):
    """ Visualize a directed multigraph using graphviz """
    nodes, edges = debruijn(st, k)
    dot_str = 'digraph "DeBruijn graph" {'
    for node in nodes:
        dot_str += '  %s [label="%s"] ;' % (node, node)
    for src, dst in edges:
        dot_str += '  %s -> %s ;' % (src, dst)
    return dot_str + '}'