#!/usr/bin/env python3
"""
Author : Tanner Bland <tannerbland@arizona.edu>
Date   : 2025-01-26
Purpose: Print greeting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print greeting',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-g',
                        '--greeting',
                        help='A greeting string',
                        metavar='str',
                        type=str,
                        default='Howdy')
    parser.add_argument('-n',
                        '--name',
                        help='A name string for the greeting',
                        metavar='str',
                        type=str,
                        default='Stranger')
    parser.add_argument('-e',
                        '--excited',
                        help='Add an exclamation point',
                        action='store_true')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    greeting = args.greeting
    name = args.name
    excited = '!' if args.excited else '.'
    print(f'{greeting}, {name}{excited}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
