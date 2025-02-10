#!/usr/bin/env python3
"""
Author : Tanner Bland <tannerbland@arizona.edu>
Date   : 2025-02-04
Purpose: divide.py; divides two numbers by one another
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Divides integer inputs by one another',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('numbers',
                        nargs=2,
                        type=int,
                        help='Two integers to divide')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Perform division"""
    args = get_args()
    num1, num2 = args.numbers
                    
    if num2 == 0:
        print('usage: divide.py [-h] INT INT')
        print('divide.py: error: Cannot divide by zero, dum-dum!')
        exit(1)
                        
    result = num1 // num2
    print(f'{num1} / {num2} = {result}')
    return result

# --------------------------------------------------
if __name__ == '__main__':
    main()
