#!/usr/bin/env python3
"""
Author : Tanner Bland <tannerbland@arizona.edu>
Date   : 2025-02-24
Purpose: Develop a python script that accepts a DNA string or a filename containing a DNA sequence and prints the reverse complement.
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print the reverse complement of DNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('DNA',
                        metavar='str',
                        help='Input sequence or file')

    return parser.parse_args()


# --------------------------------------------------
def reverse_complement(dna_sequence):
    """Return the reverse complement of the given DNA sequence."""
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join(complement[base] for base in reversed(dna_sequence))


# --------------------------------------------------
def main():
    """Main function to process DNA sequence and compute reverse complement"""

    args = get_args()
    dna_input = args.DNA

    # Try to open the input as a file
    try:
        with open(dna_input, 'r') as file:
            dna_sequence = file.read().strip() 
                            
    # If it's not a file, assume it's a DNA sequence
    except FileNotFoundError:
        dna_sequence = dna_input.strip()

    # Compute and print the reverse complement
    rev_complement = reverse_complement(dna_sequence)
    print(rev_complement)


# --------------------------------------------------
if __name__ == '__main__':
    main()
