#!/usr/bin/env python3
import re, sys

gff_file = sys.argv[1]

GeneID2locustag_dict = {}
locustag2ID_dict = {}
GeneID2Genbank_dict = {}
ID2Genbank_dict = {}
Parent2Genbank_dict = {}
ID2Parent_dict = {}
Genbank2ID_dict = {}

def NCBIgffParse1(gff_file):
    with open(gff_file) as gfffile:
        for line in gfffile:
            if line.startswith("#"):continue
            else:
                cols = line.strip().split("\t")
                core_item = cols[8].split(";")
                if cols[2] == "gene":
                   GeneID = re.search(';Dbxref=GeneID:(\w+);', cols[8]).group(1)
                   ID = re.search('ID=(\w+);', cols[8]).group(1)
                   locus_tag = re.search(';locus_tag=(\w+)', cols[8]).group(1)
                   GeneID2locustag_dict[GeneID] = locus_tag
                   locustag2ID_dict[locus_tag] = ID
                if cols[2] == "mRNA" or cols[2] == "ncRNA" or cols[2] == "rRNA" or cols[2] == "tRNA":
                   ID = re.search('ID=(\w+);', cols[8]).group(1)
                   Parent = re.search('Parent=(\w+);', cols[8]).group(1)
                   ID2Parent_dict[ID] = Parent
                if cols[2] == "mRNA" or cols[2] == "ncRNA" or cols[2] == "rRNA":
                   ID = re.search('ID=(\w+);', cols[8]).group(1)
                   Parent = re.search('Parent=(\w+);', cols[8]).group(1)
                   Genbank = re.search('Genbank:([\w\.]+)', cols[8]).group(1)
                   ID2Genbank_dict[ID] = Genbank
                   Genbank2ID_dict[Genbank] =ID
                   Parent2Genbank_dict[Parent] = Genbank
                if cols[2] == "exon" or cols[2] == "CDS":
                                   if "Genbank:" in cols[8]:
                       GeneID = re.search('GeneID:(\w+)', cols[8]).group(1)
                       Genbank = re.search('Genbank:([\w\.]+)', cols[8]).group(1)
                       if "transcript_id" in cols[8]:
                           transcript_id = re.search('transcript_id=([\w\.]+)', cols[8]).group(1)
                       elif "protein_id" in cols[8]:
                           protein_id = re.search('protein_id=([\w\.]+)', cols[8]).group(1)
                       GeneID2Genbank_dict[GeneID] = Genbank
                   else:
                       Parent = re.search('Parent=(\w+)', cols[8]).group(1)
                       GeneID2Genbank_dict[GeneID] = Parent
                else:continue
    return(GeneID2locustag_dict, GeneID2Genbank_dict, ID2Genbank_dict, Parent2Genbank_dict, ID2Parent_dict, locustag2ID_dict, Genbank2ID_dict)

GeneID2locustag, GeneID2Genbank, ID2Genbank, Parent2Genbank, ID2Parent, locustag2ID, Genbank2ID = NCBIgffParse1(gff_file)

def NCBIgff2gtf(gff_file):
    with open(gff_file) as gfffile:
        for line in gfffile:
            if line.startswith("#"):continue
            else:
                cols = line.strip().split("\t")
                core_item = cols[8].split(";")
                if cols[2] == "gene" or cols[2] == "exon" or cols[2] == "CDS":
                    core_itemtmp =  [x for x in core_item if ("gbkey=" not in x) and ("partial=" not in x)
                                     and ("product=" not in x) and ("gene_biotype=" not in x) and ("Name=" not in x)
                                     and ("end_range=" not in x) and ("start_range=" not in x) and ("transl_table=" not in x)
                                     and ("gene=" not in x)]
                    if cols[2] == "exon" or cols[2] == "CDS":
                        Parent = re.search('Parent=(\w+)', cols[8]).group(1)
                        Genbank = re.search('Genbank:([\w\.]+)', cols[8]).group(1)
                        print('\t'.join(cols[0:8]) + '\t' + 'transcript_id "' + Parent +
                              '"; gene_id "' + ID2Parent_dict.setdefault(Parent, Parent) +
                              '"; gene_name "' + Parent + '";')
#NCBIgff2gtf(gff_file)

intrans = sys.argv[2]

def transID(intrans):
    """trans locus_tag to ID in gene_info.xls"""
    with open(intrans) as infofile:
        for line in infofile:
            cols = line.strip().split("\t")
            if line.startswith("Locus tag"):
                print("ID" + "\t" + "\t".join(cols[0:]))
            else:
                print(locustag2ID_dict.setdefault(cols[0], cols[0]) + "\t" + "\t".join(cols[0:]))
transID(intrans)

def transID2(intrans):
    '''trans Genbank to ID in GO_ANNOTATION.xls'''
    with open(intrans) as infofile:
        for line in infofile:
            cols = line.strip().split("\t")
            if line.startswith("Locus tag"):
                print("Unigene_ID" + "\t" + "\t".join(cols[1:]))
            else:
                key_tmp = Genbank2ID_dict.setdefault(cols[0], cols[0])
                final_need =  ID2Parent_dict.setdefault(key_tmp, key_tmp)
                print(final_need + "\t" + "\t".join(cols[1:]))
#    print(Genbank2ID_dict)
#transID2(intrans)

def transID3(intrans):
    '''trans Genbank to ID in pathway_info.xls'''
    with open(intrans) as infofile:
        for line in infofile:
            if line.startswith("PATHWAY_ID"):
                print(line.strip())
            else:
                cols             = line.strip().split("\t")
                cols_tmp         = cols[3].split(",")
                cols_tmp_tmp     = [Genbank2ID_dict.setdefault(x, x) for x in cols_tmp]
                cols_tmp_tmp_tmp = [ID2Parent_dict.setdefault(x, x) for x in cols_tmp_tmp]
                print("\t".join(cols[0:3]) + "\t" + ",".join(cols_tmp_tmp_tmp))
#transID3(intrans)

