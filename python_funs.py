#!/usr/bin/env python3

from random import random, choice

def mutseq( sequence, mut_frac ):
    """
    This function randomly mutates a fraction of input sequences.
    Keyword arguments:
        sequence - input sequence
        mut_frac - fraction of mutated sequence
    """
    seq = list(sequence)
    for i, s in enumerate(seq):
            val = random()
            if val < mut_frac:
                # choose a random nucleotide that's different.
                seq[i] = choice([x for x in "ACTG" if x != s.upper()])
    return seq

def randomeseq( size ):
    """
    This function generates a random DNA sequence of a given size.
    Keyword arguments:
        size - the size of the sequence
    """
    return ''.join( choice( 'ATGC' ) for x in range( size ) )

def rev_comp( seq ):
    """
    This function returns the reverse complement of input DNA sequences.
    Keyword arguments:
        sequence - input sequence
    """
    return seq[::-1].translate(str.maketrans('atgcATGC','tacgTACG'))
