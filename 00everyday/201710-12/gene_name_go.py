#2017年10月18日
#客户提供一些genename或者locus tag，需要从库里根据对应的geneID,提取相应的GO注释。
#!/usr/bin/env python3
import re

def randict():
    with open("list") as randict:
        ran_dict = {}
        GeneID2gene_name_dict = {}
        GeneID2locus_tag_dict = {}
        for line in randict:
            gene_name = (re.search("\[gene=(\w+)\]", line).group(1) if "[gene=" in line else "-")
            GeneID = (re.search("\[db_xref=GeneID:(\w+)\]", line).group(1) if  "[db_xref=GeneID:" in line else "-")
            locus_tag = (re.search("\[locus_tag=(\w+)\]", line).group(1) if  "[locus_tag=" in line else "-")
            ran_dict[gene_name] = GeneID
            ran_dict[locus_tag] = GeneID
            GeneID2gene_name_dict[GeneID] = gene_name
            GeneID2locus_tag_dict[GeneID] = locus_tag
    return ran_dict, GeneID2gene_name_dict, GeneID2locus_tag_dict
myran_dict,GeneID2gene_name_dict,GeneID2locus_tag_dict = randict()

def anno_select1():
    with open("gene_name.xls") as item_file:
        item_list = []
        for m in item_file:
            mygene = (m.strip())
            anno_tmp = myran_dict.get(mygene, mygene + "_error")
            item_list.append(anno_tmp)
        return item_list
item_list = anno_select1()
def anno_select3():
    for item in item_list:
        print(item + "\t" + GeneID2locus_tag_dict.get(item,"-") + "\t" + \
              GeneID2gene_name_dict.get(item,"-"))
#anno_select3()

def anno_select4():
    anno_list = []
    with open("AL123456.3.ffn_GO2_GO_ANNOTATION.xls") as ran_anno:
        for line in ran_anno:
            cols = line.strip().split("\t")
            if cols[0] in item_list:
                print(cols[0] + "\t" + GeneID2locus_tag_dict.get(cols[0],"-") + "\t" + \
                      GeneID2gene_name_dict.get(cols[0],"-") + "\t" + \
                      "\t".join(cols[1:]))
                anno_list.append(cols[0])
    anno_list_set = list(set(anno_list))
    no_anno_list = list(set(item_list).difference(set(anno_list_set)))
#    for i in no_anno_list:
#        print(i, GeneID2gene_name_dict.get(i,"-"), GeneID2locus_tag_dict.get(i, "-"))
anno_select4()



