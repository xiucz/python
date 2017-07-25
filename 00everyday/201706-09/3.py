#!/usr/bin/env python3
import re
def fillgtf(ori_gtffile):
    with open(ori_gtffile) as myhd:
        for line in myhd.readlines():
            cols = line.strip().split("\t")
            if "=true" in line:
                locus_tag = re.search(';locus_tag=(.*?);', cols[8]).group(1)
            else:
                locus_tag = re.search(';locus_tag=(.*)', cols[8]).group(1)
            print("\t".join(cols[0:8]) + "\t" + 'gene_id "' + locus_tag + '"; transcript_id "' + locus_tag + '";')


fillgtf("GCF_001287225.1_bcg_Prague_genomic.gtf_ori")
