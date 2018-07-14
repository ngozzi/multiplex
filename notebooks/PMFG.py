"""
Create a network starting from a correlation matrix using PMFG algorithm
"""


import networkx as nx
import numpy as np
import planarity
import progressbar


def get_network_PMFG(corr_matrix): 

    #get the list of decreasing weighted links
    rholist = []
    n = len(corr_matrix)
    for i in range(n): 
        for j in range(n): 
            if i<j:
                if corr_matrix[i][j] != 0:
                    rholist.append([abs(float(corr_matrix[i][j])),i,j])
                
    rholist.sort(key=lambda x: x[0])
    rholist.reverse()
    
    m = len(rholist)
    filtered_matr = np.zeros((n, n))
    control = 0


    with progressbar.ProgressBar(max_value=m) as bar:
    #get the filtered adjacency matrix using PMFG algorithm
        for t in range(m): 
            if control <= 3 * (n - 2) - 1: 
                i = rholist[t][1]
                j = rholist[t][2]
                filtered_matr[i][j] = rholist[t][0]

                #check planarity here
                G = nx.Graph()
                for i in range(0,n): 
                    for j in range(0,n): 
                        if filtered_matr[i][j] != 0:
                            G.add_edge(int(i),int(j),weight = filtered_matr[i][j])
                if planarity.is_planar(G) == False: 
                    filtered_matr[i][j] = 0
                    control = control +1
            bar.update(t)
    
    #build the network
    PMFG = nx.Graph()
    for i in range(0,n): 
        for j in range(0,n): 
            if filtered_matr[i][j] != 0:
                PMFG.add_edge(int(i),int(j),weight = filtered_matr[i][j])
    
    return PMFG
