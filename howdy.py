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

    parser.add_argument('positional',
                        metavar='str',
                        help='A positional argument',
                        default= '')

    parser.add_argument('-h',
                        '--help',
                        help='A named string argument',
                        metavar='str',
                        type=str,
                        default= '''usage: howdy.py [-h] [-g str] [-n str] [-e]

                    Greetings and howdy

                    optional arguments:
                      -h, --help            show this help message and exit
                      -g str, --greeting str
                                            The greeting (default: Howdy)
                      -n str, --name str    Whom to greet (default: Stranger)
                      -e, --excited         Include an exclamation point (default: False)''')
                    
    parser.add_argument('-g',
                        '--greeting',
                        help='A greeting string',
                        metavar='str',
                        type=str,
                        default= 'Howdy')
                    
    parser.add_argument('-n',
                        '--name',
                        help='A name string for the greeting',
                        metavar='str',
                        type=str,
                        default= 'Stranger')
                    
    parser.add_argument('-e',
                        '--excited',
                        help='Add an exclamation point',
                        metavar= 'bool',
                        default= False,
                        action= 'store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(args.g, ',', args.n, '!' if args.excited else '', sep=' ')


# --------------------------------------------------
if __name__ == '__main__':
    main()
