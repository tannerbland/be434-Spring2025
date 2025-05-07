#!/usr/bin/env python3
"""
Author : Tanner Bland <tannerbland@arizona.edu>
Date   : 2025-04-13
Purpose: Run-length encoding of DNA
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

    parser.add_argument('str',
                       metavar='str',
                       type=str,
                       help='DNA text or file')

    return parser.parse_args()


# --------------------------------------------------
def rle(seq):
    """Perform run-length encoding on a DNA sequence"""
    if not seq:
        return ''

    compressed = []
    current_char = seq[0]
    count = 1

    for char in seq[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(current_char + (str(count) if count > 1 else ''))
            current_char = char
            count = 1

    compressed.append(current_char + (str(count) if count > 1 else ''))
    return ''.join(compressed)


# --------------------------------------------------
def process_input(input_str):
    """Determine if input is a file or sequence and process accordingly"""
    if os.path.isfile(input_str):
        with open(input_str, 'rt', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:  # Skip empty lines
                    yield rle(line)
    else:
        yield rle(input_str)


# --------------------------------------------------
def main():
    """Main program logic"""
    args = get_args()
    try:
        for encoded in process_input(args.str):
            print(encoded)
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(1)


# --------------------------------------------------
if __name__ == '__main__':
    main()