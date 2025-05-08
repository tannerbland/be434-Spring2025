#!/usr/bin/env python3
"""
Author: Tanner Bland <tannerbland@arizona.edu>
Purpose: Encode or decode text using a Vigenere cipher
"""

import argparse

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='vigenere cipher',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        type=argparse.FileType('rt'),
                        help='Input file')

    parser.add_argument('-k',
                        '--keyword',
                        default='CIPHER',
                        help='A keyword')

    parser.add_argument('-d',
                        '--decode',
                        action='store_true',
                        help='A boolean flag')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file (default: std.out)')

    return parser.parse_args()


# --------------------------------------------------
def shift_char(c, k, decode=False):
    """Shift character `c` using character `k` as key"""

    if not c.isalpha():
        return c

    alpha = ord('A')
    c_idx = ord(c.upper()) - alpha
    k_idx = ord(k.upper()) - alpha

    if decode:
        shift = (c_idx - k_idx) % 26
    else:
        shift = (c_idx + k_idx) % 26

    return chr(shift + alpha)


# --------------------------------------------------
def vigenere(text, keyword, decode=False):
    """Apply the Vigenere cipher to the text with the given keyword"""

    keyword = keyword.upper()
    k_len = len(keyword)
    output = []

    for line in text.splitlines(keepends=True):
        k_index = 0
        for char in line:
            if char.isalpha():
                k = keyword[k_index % k_len]
                output.append(shift_char(char, k, decode))
                k_index += 1
            else:
                output.append(char)

    return ''.join(output).rstrip()


# --------------------------------------------------
def main():
    """Main program logic"""

    args = get_args()
    input_text = args.FILE.read()
    output_text = vigenere(input_text, args.keyword, args.decode)

    if args.outfile:
        with open(args.outfile, 'wt') as out_fh:
            out_fh.write(output_text + '\n')
    else:
        print(output_text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
