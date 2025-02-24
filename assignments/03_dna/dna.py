#!/usr/bin/env python3
"""
Author : Tanner Bland <tannerbland@arizona.edu>
Date   : 2025-02-24
Purpose: Develop a python script that will accept a sequence of DNA as a single positional argument to count tetranucleotide frequency.
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('DNA',
                        metavar='str',
                        help='Input DNA sequence')

    return parser.parse_args()
                    
# --------------------------------------------------
def count_bases(dna_sequence):
    """Count the frequency of bases A, C, G, T in the DNA sequence."""
    base_counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    # Iterate over each character in the sequence and count the occurrences
    for base in dna_sequence:
        if base in base_counts:
            base_counts[base] += 1

    return base_counts

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    dna_sequence = args.DNA

    # Count the base frequencies
    base_counts = count_bases(dna_sequence)

    # Print the frequencies of A, C, G, and T
    print(base_counts['A'], base_counts['C'], base_counts['G'], base_counts['T'])


# --------------------------------------------------
if __name__ == '__main__':
    main()
