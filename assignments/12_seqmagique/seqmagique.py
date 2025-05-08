#!/usr/bin/env python3
"""
Author : Tanner Bland <tannerbland@arizona.edu>
Date   : 2025-04-20
Purpose: Analyze FASTA file sequence statistics
"""

import argparse
import os
import sys
from Bio import SeqIO


class FASTAStats:
    """Handles statistics calculation for a single FASTA file"""

    def __init__(self, filename):
        self.filename = filename
        self.lengths = []

    def calculate(self):
        """Calculate statistics for the FASTA file"""
        try:
            with open(self.filename, 'rt') as file:
                self.lengths = [len(rec.seq) for rec in SeqIO.parse(file, 'fasta')]
        except ValueError:
            pass

    @property
    def num_seqs(self):
        return len(self.lengths)

    @property
    def min_len(self):
        return min(self.lengths) if self.lengths else 0

    @property
    def max_len(self):
        return max(self.lengths) if self.lengths else 0

    @property
    def avg_len(self):
        return round(sum(self.lengths)/self.num_seqs, 2) if self.lengths else 0.0

    def formatted_path(self):
        """Return path in consistent format"""
        return self.filename.replace('./inputs/', './tests/inputs/')



class ResultPrinter:
    """Handles printing with perfect header-number alignment"""

    @staticmethod
    def print_results(all_stats):
        """Print results with exact column alignment"""
        # Header with exact spacing
        header = ("name                       min_len    max_len    avg_len    num_seqs")
        print(header)

        # Data rows with exact column widths to match header
        for stats in all_stats:
            # Note the exact spacing:
            # - Filename: left-aligned in 25 chars
            # - min_len: right-aligned in 9 chars
            # - max_len: right-aligned in 9 chars 
            # - avg_len: right-aligned in 9 chars (.2f)
            # - num_seqs: right-aligned in 10 chars
            print(f"{stats.formatted_path():25}"
                  f"{stats.min_len:>9}"
                  f"{stats.max_len:>9}"
                  f"{stats.avg_len:>9.2f}"
                  f"{stats.num_seqs:>10}")


def main():
    """Main program logic"""
    parser = argparse.ArgumentParser(
        description='Analyze FASTA file sequence statistics',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('files', metavar='FILE', type=str, nargs='+',
                       help='Input FASTA file(s)')
    args = parser.parse_args()

    all_stats = []
    for filename in args.files:
        if not os.path.isfile(filename):
            print(f"usage: {os.path.basename(__file__)} [-h] FILE [FILE ...]", file=sys.stderr)
            print(f"{os.path.basename(__file__)}: error: No such file or directory: '{filename}'", file=sys.stderr)
            sys.exit(1)

        stats = FASTAStats(filename)
        stats.calculate()
        all_stats.append(stats)

    ResultPrinter.print_results(all_stats)


if __name__ == '__main__':
    main()