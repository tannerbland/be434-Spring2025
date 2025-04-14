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
                        type=argparse.FileType('r'),
                        help='Input file with aligned sequences')

    return parser.parse_args()


# --------------------------------------------------
def parse_sequences(file):
    """Parse the input file and return a list of sequences"""
    return [line.strip() for line in file if line.strip()]


# --------------------------------------------------
def find_conserved(sequences):
    """Return a string showing conserved (|) and variable (X) positions"""
    if not sequences:
        return ''

    length = len(sequences[0])
    if not all(len(seq) == length for seq in sequences):
        sys.exit('Error: All sequences must be the same length.')

    result = ''
    for i in range(length):
        chars = [seq[i] for seq in sequences]
        if all(c == chars[0] for c in chars):
          result += '|'
        else:
            result += 'X'

    return result


# --------------------------------------------------
def main():
    """Main program logic"""

    args = get_args()
    sequences = parse_sequences(args.FILE)

    for seq in sequences:
        print(seq)

    conserved = find_conserved(sequences)
    print(conserved)


# --------------------------------------------------
if __name__ == '__main__':
    main()
