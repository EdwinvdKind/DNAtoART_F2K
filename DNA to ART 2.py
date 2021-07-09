# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 13:15:27 2021

@author: evdki
"""

def generatekmerlist(filename, kmerlength):
    sequences = []
    counter = 0
    kmerlist = []
    kmers = []
    with open(filename) as fastadata:
        readfasta = fastadata.read()
        genes = readfasta.split(">")
        
        for gene in genes:
            seq = gene.replace("-",'').split('\n')
            emptystring = ''
            sequences.append(emptystring.join(seq[1::]))

    for x in sequences:        
        while counter <= len(x):
            if len(x[counter:(counter+kmerlength)]) < kmerlength:
                counter += kmerlength
            elif len(x[counter:(counter+kmerlength)]) >= kmerlength:  
                kmers.append(x[counter:(counter+kmerlength)])
            else:
                None
            counter += 1
        
        kmerlist.append(kmers)

    return kmerlist

print(generatekmerlist('lutea_16_spore_DMSO_ITS4_CUT_group1.fas',5))




