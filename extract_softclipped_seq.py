#!/usr/bin/env python

import sys, pysam, argparse

def get_parser():
    desc = "Extract soft-clipped sequences from mapped reads. Fasta is outputted."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('AlignmentFile', type=str, \
        help="SAM/BAM file, will guess by suffix, default: bam")
    parser.add_argument('-t', '--threshold', type=int, default=0, \
        help="set this parameter to only report soft clipped regions larger than the threshold")
    return parser

def get_digit( cigar, end ):
    
    int_digit = ""
    if end: 
        for a in cigar[::-1][1:]:
            if a.isdigit(): int_digit = a + int_digit
            else: break
    else: 
        for a in cigar:
            if a.isdigit(): int_digit = int_digit + a 
            else: break
    return int(int_digit)

def print_softclip_seq( threshold, cigar, qname, seq, end=False ):

    int_digit = get_digit( cigar, end )

    if int_digit < threshold: return True

    if end: sclipped = seq[ len(seq)-int_digit: ]
    else: sclipped = seq[ :int_digit ]

    print(">%s_%s\n%s" % (qname, cigar, sclipped))
    return True

def run_extraction( samfile, threshold ):
    for read in samfile.fetch():
        # check for softclip, if no softclip, index returns ValueError
        try: idx = read.cigarstring.index("S")
        except: continue
        # softclip at 3' end
        if read.cigarstring.endswith("S"): 
            print_softclip_seq( threshold, read.cigarstring, read.qname, read.seq, end=True )
        # softclip at 5' end
        if idx < len(read.cigarstring) - 1:         
            print_softclip_seq( threshold, read.cigarstring, read.qname, read.seq )

def main():
    parser = get_parser()
    args = parser.parse_args()
    fname = args.AlignmentFile
    threshold = args.threshold
    
    # guess sam or bam format based on suffix
    if fname.endswith("sam"): samfile = pysam.AlignmentFile(fname, "r")
    else: samfile = pysam.AlignmentFile(fname, "rb")
    
    run_extraction( samfile, threshold )

main()
