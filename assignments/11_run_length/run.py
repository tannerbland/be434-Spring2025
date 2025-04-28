#!/usr/bin/env python3
"""
Author : Tanner Bland <tannerbland@arizona.edu>
Date   : 2025-04-13
Purpose: Run-length encoding of DNA sequences
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='DNA text or file')

    return parser.parse_args()


# --------------------------------------------------
def rle(seq):
    """Run-length encode a DNA sequence"""

    if not seq:
        return ''

    encoded = []
    count = 1
    prev = seq[0]

    for char in seq[1:]:
        if char == prev:
            count += 1
        else:
            encoded.append(prev + (str(count) if count > 1 else ''))
            prev = char
            count = 1

    encoded.append(prev + (str(count) if count > 1 else ''))

    return ''.join(encoded)


# --------------------------------------------------
def main():
    """Main program"""

    args = get_args()
    arg = args.text

    # Determine if the input is a file
    if os.path.isfile(arg):
        with open(arg, 'rt') as fh:
            for line in fh:
                line = line.strip()
                if line:
                    print(rle(line))
    else:
        print(rle(arg))


# --------------------------------------------------
def test_rle():
    """Unit test for rle function"""
    assert rle('') == ''
    assert rle('A') == 'A'
    assert rle('ACGT') == 'ACGT'
    assert rle('AA') == 'A2'
    assert rle('AAAAA') == 'A5'
    assert rle('ACCGGGTTTT') == 'AC2G3T4'


# --------------------------------------------------
if __name__ == '__main__':
    main()
