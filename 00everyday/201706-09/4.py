#!/usr/bin/env python3
import sys
import pandas as pd
import numpy as np
## 20170731
infile1, infile2, infile3  = sys.argv[1], sys.argv[2], sys.argv[3]
def shared_gene():
    '''python3 shared_gene.py all.counts.G3_vs_G1.edgeR_differential.xls all.counts.G4_vs_G1.edgeR_differential.xls \
               all.counts.G3_vs_G1.edgeR_differential.xls'''
    hf1, hf2 = pd.read_table(infile1), pd.read_table(infile2)
    hf1_geneid, hf2_geneid = list(hf1["gene id"]), list(hf2["gene id"])
    shared_geneid = [val for val in hf1_geneid if val in hf2_geneid]
 
    with open(infile3) as myfile:
        for line in myfile:
            cols = line.strip().split("\t")
            if cols[0] in shared_geneid:
                print(line.strip(),)
            else:continue
#shared_gene()
 
def shared_gene2():
    hf1, hf2 = pd.read_table(infile1), pd.read_table(infile2)
    shared_geneid = pd.merge(hf1["gene id"], hf2, left_on = "gene id", right_on = "gene id",how = "inner")
 
## 20170801
def G3vsG1_FC3():
    with open("all.counts.G3_vs_G1.edgeR_differential.xls_backup") as FCfile:
        for line in FCfile:
            line_tmp = line.strip()
            cols = line_tmp.split("\t")
           if line.startswith("gene id"):
               print(line_tmp)
            elif float(cols[12]) > 8 or float(cols[12]) < -8:
               print(line_tmp)
G3vsG1_FC3()
