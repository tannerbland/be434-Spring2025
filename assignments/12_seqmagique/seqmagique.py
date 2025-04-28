#!/usr/bin/env python3
"""
Author : Tanner Bland <tannerbland@arizona.edu>
Date   : 2025-04-27
Purpose: Summarize FASTA files: min/max/avg lengths and number of sequences
"""

import argparse
import sys
import os
from Bio import SeqIO
from tabulate import tabulate

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Summarize FASTA files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files', 
                        metavar='FILE', 
                        nargs='+',
                        help='Input FASTA file(s)')

    parser.add_argument('-t',
                        '--tablefmt',
                        default='plain',
                        choices=['plain', 'simple'],
                        help='Table format style')

    return parser.parse_args()


# --------------------------------------------------
def process_fasta(file):
    """Process FASTA file and return sequence lengths using BioPython"""
    lengths = []

    with open(file) as fh:
        for record in SeqIO.parse(fh, "fasta"):
            lengths.append(len(record.seq))

    return lengths


# --------------------------------------------------
def summarize_fasta(files):
    """Summarize FASTA files: min/max/avg lengths and number of sequences"""
    headers = ['name', 'min_len', 'max_len', 'avg_len', 'num_seqs']
    rows = []

    for file in files:
        if not os.path.exists(file):
            print(f"Usage: {sys.argv[0]} [FILE]...")
            print(f"No such file or directory: '{file}'")
            sys.exit(1)

        lengths = process_fasta(file)
        num = len(lengths)
        stats = (
            min(lengths) if num else 0,
            max(lengths) if num else 0,
            sum(lengths) / num if num else 0,
            num
        )
        rows.append([file, *stats[:3], stats[3]])

    return rows, headers


# --------------------------------------------------
def main():
    """Main program logic"""

    args = get_args()
    rows, headers = summarize_fasta(args.files)

    print(tabulate(rows, headers=headers, tablefmt=args.tablefmt))


# --------------------------------------------------
if __name__ == '__main__':
    main()
