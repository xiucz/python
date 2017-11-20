#!/usr/bin/env python3
import argparse

def go_select(f1, c1, f2, c2, outf, combine=True):
    D1 = {}
    f_handle1 = open(f1, 'r')
    for line in f_handle1:
        fp_one = line.rstrip().split("\t")
        D1[fp_one[c1-1]] = line.rstrip()
    f_handle1.close()

    out_Handle = open(outf, "w")

    f_handle2 = open(f2, 'r')
    for line in f_handle2:
        fp_two = line.rstrip().split("\t")
        if c2 <= len(fp_two) and fp_two[c2-1] in D1:
            TC = fp_two[c2-1]
            if combine == True:
                out_Handle.write("{0}\t{1}\n".format(D1[TC], line.rstrip()))
            else:
                out_Handle.write("{0}\n".format(line.rstrip()))
    out_Handle.close()
    f_handle2.close()


if __name__ == "__main__":

    USAGE = "Define input file containing variant sites"

    parser = argparse.ArgumentParser(description = USAGE)
    parser.add_argument("-ia", "--inputa", action = "store", required = True, help = "the input file a")
    parser.add_argument("-ib", "--inputb", action = "store", required = True, help = "the input file b")
    parser.add_argument("-o", "--output", action = "store", default="Output_columns_selected.txt" , help = "the output file")
    parser.add_argument("-a", action = "store", type=int, help = "column of input a")
    parser.add_argument("-b", action = "store", type= int,  help = "column of input b")
    parser.add_argument("-c", "--co", action = "store_true", default = False,  help = "combine file a and file b or not ? ")
    args = parser.parse_args()

    combincol = False
    if args.co == True:
        combincol = True
    go_select(args.inputa, args.a, args.inputb, args.b, args.output,  combincol)
