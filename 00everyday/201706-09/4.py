#### 20170731
#!/usr/bin/env python3
import sys
import pandas as pd
import numpy as np

infile1, infile2, infile3  = sys.argv[1], sys.argv[2], sys.argv[3]
def shared_gene():
    '''python3 shared_gene.py all.counts.G3_vs_G1.edgeR_differential.xls all.counts.G4_vs_G1.edgeR_differential.xls \
               all.counts.G3_vs_G1.edgeR_differential.xls'''
    hf1, hf2 = pd.read_table(infile1), pd.read_table(infile2)
    hf1_geneid, hf2_geneid = list(hf1["gene id"]), list(hf2["gene id"])
    shared_geneid = [val for val in hf1_geneid if val in hf2_geneid]

    with open(infile3) as myfile:
        for geneid in shared_geneid:
            for line in myfile:
                cols = line.strip().split("\t")
                if geneid in cols[0]:
                    print(line,)
                else:
                    print("hha~~~")

shared_gene()
