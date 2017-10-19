#!/usr/bin/env python3
import glob

def fq_rename():
    fq_files = glob.glob("trim_13_FC_*fastq")
    for fq_file in fq_files:
        sample = fq_file.split('.fastq')[0].split('trim_')[1]
        print(sample)
        output = open(sample+'_rename.fastq', 'w')
        with open(fq_file) as ranfile:
            count = 0
            while 1:
                try:
                    count += 1
                    a, b, c, d = next(ranfile), next(ranfile), \
                                 next(ranfile), next(ranfile)
                    output.write("@" + sample + "_" + str(count) + \
                                 "\n" + b + c + d)
                except StopIteration:
                    break
        output.close()
fq_rename()
