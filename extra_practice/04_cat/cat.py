#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-09-29
Purpose: concat
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Concat',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        help='A readable file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'))

    parser.add_argument('-n',
                        '--number',
                        help='A boolean flag',
                        action='store_true')

    # args = parser.parse_args()
    # if not 3 <= len(args.files) <= 5:
    #     parser.error('Must have 3-5 files')

    # return args

    return parser.parse_args()


# --------------------------------------------------
def main():
    """cat"""

    args = get_args()

    # for fh in args.files:
    #     line_num = 0
    #     for line in fh:
    #         line_num += 1
    #         # print(line, end='')
    #         if args.number:
    #             print('{:>6}\t{}'.format(line_num, line.rstrip()))
    #         else:
    #             print(line, end='')

    for fh in args.files:
        for line_num, line in enumerate(fh, start=1):
            if args.number:
                #print(f'{line_num:>6}\t{line.rstrip()}')
                print(f"{str(line_num).rjust(6)}\t{line.strip()}")
            else:
                print(line, end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
