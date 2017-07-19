#### fastq_to_fasta.py 20170719
#!/usr/bin/env python
import sys

if(len(sys.argv) < 2):
        sys.exit('python fastq_to_fasta.py 1.fastq [2.fastq, ...]')

fq_files = sys.argv[1:]
for fq_file in fq_files:
        sample = fq_file.split('.fastq')[0]
        output = open(sample+'.fa', 'w')

        with open(fq_file, 'r') as input:
                while 1:
                        try:
                                a, b, c, d = next(input), next(input), next(input), next(input)

                                output.write('>'+a+b)
                        except StopIteration:
                                break

        output.close()
