#### 20170630 filter_gtf.py
#!/usr/bin/env python3
def ref_file_id(refid):
    ref_id = []
    myin1 = open(refid)
    for line in myin1.readlines():
        ref_id.append(line.strip())
    return ref_id


def read_gft(Triticum_aestivumgtf_ori_3):
    with open(Triticum_aestivumgtf_ori_3) as myin2:
        for line in myin2.readlines():
            cols = line.strip().split("\t")
            if cols[0] in ref_id:
                print("\t".join(cols[:]))
            else:continue
ref_id = ref_file_id("ref.id")
read_gft("Triticum_aestivum.gtf_ori_3")


#### 20170630 gtf2gtf_bed.py
#!/usr/bin/env python3
import re
def gtf2gtf_bed(gtf_file):
    with open(gtf_file) as myhd:
        for line in myhd:
            cols = line.strip().split("\t")
            myname = re.search('gene_id "(.*)"; transcript_id "', cols[8]).group(1)
            print(cols[0] + "\t" + "\t".join(cols[3:5]) + "\t" + cols[2] + "\t" + myname + "\t" + cols[1])

gtf2gtf_bed("Triticum_aestivum.gtf")


#### 20170630 

#!/usr/bin/env python3
import re
def fillgtf(ori_gtffile):
    with open(ori_gtffile) as myhd:
        for line in myhd.readlines():
            cols = line.strip().split("\t")
            if "geneID" in cols[8]:
                cols[8] = cols[8].replace("geneID", "gene_ID")
                print("\t".join(cols))
            else:
                mynewcols9_for, myid = re.search('(transcript_id\s"(.*)";)', cols[8]).group(1), \
                                       re.search('(transcript_id\s"(.*)";)', cols[8]).group(2)
                mynewcols8 = mynewcols9_for + " " +'gene_ID "' + myid + '";'
                print("\t".join(cols[0:8]) + "\t" + mynewcols8)
                

fillgtf("Triticum_aestivum_ori.gtf")


####20170630 fillgtf.py
import re,sys

f = open(sys.argv[1])

for line in f:
    line=line.split()
    if len(line)==9:
        if line[2]=="gene":
            regex = re.compile(r";locus_tag=(.*?);")
            a = regex.findall(line[8])
            if a:
                a=a[0]
                print("\t".join(line[0:8])+"\t"+'''gene_id "%s"; transcript_id "%s";'''%(a,a))
                print("\t".join(line[0:2])+"\t"+"exon"+"\t"+"\t".join(line[3:8])+"\t"+'''gene_id "%s"; transcript_id "%s";'''%(a,a))
            else:
                regex = re.compile(r";locus_tag=(.*)")
                a=regex.findall(line[8])
                a=a[0]
                print("\t".join(line[0:8])+"\t"+'''gene_id "%s"; transcript_id "%s";'''%(a,a))
                print("\t".join(line[0:2])+"\t"+"exon"+"\t"+"\t".join(line[3:8])+"\t"+'''gene_id "%s"; transcript_id "%s";'''%(a,a))

                
#### 20170712
import sys,re
f = open(sys.argv[1])
f1 = open("ues.gene","w")
for i in f:
        i =i.strip().split("\t")
        if i[2]=="gene":
                regex=re.compile(r"gene_id \"(.*?)\";")
                id = regex.findall(i[-1])[0]
                f1.write(i[0]+"\t"+i[3]+'\t'+i[4]+'\t'+id+'\t'+id+'\t'+i[6]+'\n')

       
#### 20170712
import sys,re
f = open(sys.argv[1])
f1 = open("ues.gene","w")
for i in f:
        i =i.strip().split("\t")
        if i[2]=="gene":
                regex=re.compile(r"gene_id \"(.*?)\";")
                id = regex.findall(i[-1])[0]
                f1.write(i[0]+"\t"+i[3]+'\t'+i[4]+'\t'+id+'\t'+id+'\t'+i[6]+'\n')


#### 20170714 transcriptome2gene
#!/usr/bin/env python3
# -*- coding:uft-8 -*-
#需要改进的Unigene_LIST的\t改成，
#去掉每行末尾的\t和字典替换#
import re, sys

def transcript_gene():
    mydict = {}
    with open("Triticum_aestivum.TGACv1.35.gtf") as infile:
        for line in infile:
            if line.startswith("#"):continue
            else:
                cols = line.strip().split("\t")
                if "transcript_id" in cols[8]:
                    item_target = re.search('gene_id "(.*)"; transcript_id "(.*)"; exon_number', cols[8])
                    if item_target:
                        gene_id, transcript_id = item_target.group(1), item_target.group(2)
                        if transcript_id not in mydict.keys():
                            mydict[transcript_id] = []
                            mydict[transcript_id].append(gene_id)
                        else:
                            mydict[transcript_id].append(gene_id)
                    else:continue
                else:continue
    newdict = {}
    for keys, values in mydict.items():
        newdict[keys] = list(set(values))
    return newdict
transcript_gene_dict = transcript_gene()

def pathway_transid():
    pathwayout = open("pathway_info.xls", "w")
    with open("pathway_info.xls_ori") as pathwayfile:
        for line in pathwayfile:
            cols = line.strip().split("\t")
            cols_tmp = cols[3]
            item_tmp = cols_tmp.split(",")
            if line.startswith("PATHWAY_ID"):
                pathwayout.write(line)
            else:
                cols_tmp_new = [transcript_gene_dict.get(x,"#")[0] for x in item_tmp]
                pathwayout.write("\t".join(cols[0:3]) + "\t" + "\t".join(cols_tmp_new) + "\n")
pathway_transid()

def ec_transid():
    ecout = open("ec_info.xls", "w")
    with open("ec_info.xls_ori") as ecfile:
        for line in ecfile:
            cols = line.strip().split("\t")
            if line.startswith("Unigene_id"):
                ecout.write(line)
            else:
                if cols[0] in transcript_gene_dict.keys():
                    ecout.write(transcript_gene_dict[cols[0]][0] + "\t" + "\t".join(cols[1:]) + "\n")
                else:continue
ec_transid()
