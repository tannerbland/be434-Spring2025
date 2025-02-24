#!/usr/bin/env python3
"""
Author : Tanner Bland <tannerbland@arizona.edu>
Date   : 2025-02-24
Purpose: Compute GC content of DNA sequences in a FASTA file or from STDIN.
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Compute GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        nargs='?',
                        type=argparse.FileType('r'),
                        default=sys.stdin,
                        help='Input sequence file (or stdin if not specified)')

    return parser.parse_args()


# --------------------------------------------------
def compute_gc_content(dna_sequence):
    """Calculate GC content of a DNA sequence as a percentage"""
    length = len(dna_sequence)
    if length == 0:
        return 0
        
    gc_count = 0
    for base in dna_sequence:
        if base in 'GC':
            gc_count += 1

    return (gc_count / length) * 100


# --------------------------------------------------
def parse_fasta(file) -> list:
    """Parse a FASTA file or input and return a list of tuples (id, sequence)"""
    sequences = []
    sequence_id = None
    sequence = []

    for line in file:
        line = line.rstrip()
        if line[0] == '>':
            if sequence_id:
                sequences.append((sequence_id, ''.join(sequence)))
            sequence_id = line[1:]
            sequence = []
        else:
            sequence.append(line)

    if sequence_id:
        sequences.append((sequence_id, ''.join(sequence)))

    return sequences


# --------------------------------------------------
def print_usage_and_exit(file_path: str = ''):
    """Print usage information and exit"""
    print('''usage: cgc.py [-h] FILE

Compute GC content

positional arguments:
  FILE        Input sequence file

optional arguments:
  -h, --help  show this help message and exit''')

    if file_path:
        # Print the error message with the original case
        print(f"no such file or directory: '{file_path}'", file=sys.stderr)


# --------------------------------------------------
def main():
    """Main function to compute GC content for each sequence"""

    args = get_args()

    # Handle input from stdin if specified
    if args.FILE == '-':
        file = sys.stdin
    else:
        file = args.FILE

    # Parse the input FASTA file
    sequences = parse_fasta(file)

    # Compute GC content for each sequence
    max_gc_content = -1
    max_gc_id = ''
    for seq_id, seq in sequences:
        gc_content = compute_gc_content(seq)
        if gc_content > max_gc_content:
            max_gc_content = gc_content
            max_gc_id = seq_id

    # Print the sequence ID with the highest GC content
    print(f'{max_gc_id} {max_gc_content:.6f}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
