#!/usr/bin/env python3
import re, sys

def gff_dict(gff_file):
    locustag2oldlocustag = {}
    geneid2locustag = {}
    with open(gff_file) as gffhd:
        for line in gffhd:
            cols = line.strip().split("\t")
            if line.startswith("#"):continue
            elif "gene" in cols[2]:
                locus_tag = re.search(";locus_tag=(\w+)", line).group(1)
                old_locus_tag_tmp = re.search(";old_locus_tag=(\w+)", line)
                old_locus_tag = (old_locus_tag_tmp.group(1) if old_locus_tag_tmp else "-")
                gene_id = re.search(";Dbxref=GeneID:(\w+);", line).group(1)
                geneid2locustag[gene_id] = locus_tag
                locustag2oldlocustag[locus_tag] = old_locus_tag
            else:continue
    return geneid2locustag, locustag2oldlocustag

def write_file():
    with open(infile) as inhd:
        headers = inhd.readline()
        header = headers.strip().split("\t")
        if change_type == "locustag2oldlocustag":
            outfile.write(header[0] + "\t" + "old_locus_tag" + "\t" + "\t".join(header[1:]) + "\n")
            for line in inhd:
                cols = line.strip().split("\t")
                outfile.write(cols[0] + "\t" + locustag2oldlocustag_dict.get(cols[0]) + "\t" + "\t".join(cols[1:]) + "\n")
        elif change_type == "geneid2locustag":
            outfile.write(header[0] + "\t" + "locus_tag" + "\t" + "\t".join(header[1:]) + "\n")
            for line in inhd:
                cols = line.strip().split("\t")
                outfile.write(cols[0] + "\t" + geneid2locustag_dict.get(cols[0]) + "\t" + "\t".join(cols[1:]) + "\n")  
    outfile.close()

if __name__ == "__main__":
    USAEG = """
    USAGE: python3 %s <change_type> <sample[.gff]> <all[.diff.xls]> <add_all[.diff.xls]>
    Example1: python3 %s locustag2oldlocustag use.gff all.counts.*.edgeR_all.xls add2locustag_all.counts.*.edgeR_all.xls
    Example12 python3 %s geneid2locustag use.gff all.counts.*.edgeR_all.xls add2oldlocustag_all.counts.*.edgeR_all.xls
    """#%(sys.argv[0], sys.argv[0], sys.argv[0], sys.argv[0], sys.argv[0])
    if len(sys.argv) != 5:
        sys.exit(USAEG)
    change_type, gff_file, infile , outfile = sys.argv[1], sys.argv[2], sys.argv[3], open(sys.argv[4], "w")
    
    geneid2locustag_dict, locustag2oldlocustag_dict = gff_dict(gff_file)
    write_file()

