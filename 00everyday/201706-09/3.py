#!/usr/bin/env python3
import re
def Prokaryotic_gff2gtf(gff_file):
    with open(gff_file) as gfffile:
        for line in gfffile:
            if line.startswith("#"):continue
            else:
                cols = line.strip().split("\t")
                if cols[2] == "gene":
                   core_item = cols[8].split(";")
                   if "locus_tag=" in core_item[-1] and "old_locus_tag=" not in core_item[-1]:
                       locus_tag = re.search(';locus_tag=(.*)', cols[8]).group(1)
                   else:
                       locus_tag = re.search(';locus_tag=(.*?);', cols[8]).group(1)
                   print("\t".join(cols[0:8]) + "\t" + 'gene_id "' + locus_tag + '"; transcript_id "' + locus_tag + '";')
                   print("\t".join(cols[0:2]) + "\t" + "exon" + "\t" + "\t".join(cols[3:8]) + "\t" +'gene_id "' + \
                         locus_tag + '"; transcript_id "' + locus_tag + '";')
                else:continue
Prokaryotic_gff2gtf("GCF_000162295.1_ASM16229v1_genomic.gff")

def fillgtf(ori_gtffile):
    with open(ori_gtffile) as myhd:
        for line in myhd.readlines():
            cols = line.strip().split("\t")
            core_item = cols[8].split(";")
            if "locus_tag=" in core_item[-1] and "old_locus_tag=" not in core_item[-1]:
                locus_tag = re.search(';locus_tag=(.*)', cols[8]).group(1)
            else:
                locus_tag = re.search(';locus_tag=(.*?);', cols[8]).group(1)
            print("\t".join(cols[0:8]) + "\t" + 'gene_id "' + locus_tag + '"; transcript_id "' + locus_tag + '";')
