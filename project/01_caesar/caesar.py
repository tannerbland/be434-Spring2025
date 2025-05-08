#!/usr/bin/env python3
"""
Author: Your Name
Purpose: Encode or decode text using a Caesar cipher
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Caesar cipher',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=str,
                        help='Input file')

    parser.add_argument('-n',
                        '--shift',
                        metavar='int',
                        type=int,
                        default=3,
                        help='Shift value (for encoding/decoding)')

    parser.add_argument('--decode',
                        action='store_true',
                        help='Decode instead of encode')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main program logic"""

    args = get_args()

    if not os.path.isfile(args.file):
        print(f"Usage: {os.path.basename(__file__)} [-h] [-n NUM] [--decode] FILE")
        print(f"No such file or directory: '{args.file}'")
        sys.exit(1)


    text = open(args.file, 'rt').read()
    shift = -args.shift if args.decode else args.shift
    print(caesar(text, shift))


# --------------------------------------------------
def caesar(text: str, shift: int) -> str:
    """Apply Caesar cipher to text"""

    result = []

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr(base + (ord(char) - base + shift) % 26)
            result.append(new_char.upper())
        else:
            result.append(char.upper())

    return ''.join(result).rstrip()


# --------------------------------------------------
if __name__ == '__main__':
    main()
