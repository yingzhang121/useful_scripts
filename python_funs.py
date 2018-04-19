#!/usr/bin/env python3

from random import random, choice

def mutseq( sequence, mut_freq ):
    seq = list(sequence)
    for i, s in enumerate(seq):
            val = random()
            if val < mut_freq:
                # choose a random nucleotide that's different.
                seq[i] = choice([x for x in "ACTG" if x != s.upper()])
    return seq

def randomeseq( size ):
    return ''.join( choice( 'ATGC' ) for x in range( size ) )

def rev_comp( seq ):
    return seq[::-1].translate(str.maketrans('atgcATGC','tacgTACG'))
