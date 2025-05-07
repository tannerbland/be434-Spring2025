#!/usr/bin/env python3
"""
Author : Tanner Bland <tannerbland@arizona.edu>
Date   : 2025-04-13
Purpose: Find conserved bases in aligned sequences from a file
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find conserved bases',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                       metavar='FILE',
                       type=argparse.FileType('rt'),
                       help='Input file with aligned sequences')

    return parser.parse_args()


# --------------------------------------------------
def parse_sequences(file):
    """Parse the input file and return a list of sequences"""
    sequences = []

    for line in file:
        line = line.strip()
        # Skip empty lines and FASTA headers if present
        if line and not line.startswith('>'):
            sequences.append(line)

    return sequences


# --------------------------------------------------
def find_conserved(sequences):
    """Return a string showing conserved (|) and variable (X) positions"""
    result = []
    for bases in zip(*sequences):
        if all(b == bases[0] for b in bases):
            result.append('|')
        else:
            result.append('X')
    return ''.join(result)


# --------------------------------------------------
def main():
    """Main program logic"""
    args = get_args()
    sequences = parse_sequences(args.FILE)
    args.FILE.close()

    if len(sequences) < 2:
        print('Error: At least two sequences are required for comparison.', file=sys.stderr)
        sys.exit(1)

    if not all(len(seq) == len(sequences[0]) for seq in sequences):
        print('Error: All sequences must be the same length.', file=sys.stderr)
        sys.exit(1)

    # Print sequences and conservation pattern
    print('\n'.join(sequences))
    print(find_conserved(sequences))


# --------------------------------------------------
if __name__ == '__main__':
    main()