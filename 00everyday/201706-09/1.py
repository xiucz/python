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

