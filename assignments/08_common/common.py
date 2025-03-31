#!/usr/bin/env python3
"""
Author : Tanner Bland <tannerbland@arizona.edu>
Date   : 2025-03-31
Purpose: Find common words between two files
"""

import argparse
import os
import sys
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common words between two files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        metavar='FILE1',
                        help='Input file 1')

    parser.add_argument('FILE2',
                        metavar='FILE2',
                        help='Input file 2')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file (default: stdout)',
                        metavar='FILE',
                        type=str,
                        default=None)

    return parser.parse_args()

# --------------------------------------------------
def get_words(filehandle):
    """Helper function to get words from a file, keeping punctuation attached to the words."""
    words = set()
    for line in filehandle:
        for word in line.split():
            cleaned_word = re.sub(r'[^\w,.\'-]', '', word) 
            if cleaned_word:
                words.add(cleaned_word)
    return words

# --------------------------------------------------
def main():
  """Find and print common words between two files"""

  args = get_args()

  try:
      if not os.path.isfile(args.FILE1):
          print(f"No such file or directory: '{args.FILE1}'")
          sys.exit(1) 

      if not os.path.isfile(args.FILE2):
          print(f"No such file or directory: '{args.FILE2}'")
          sys.exit(1) 

      with open(args.FILE1, 'r') as file1, open(args.FILE2, 'r') as file2:
          words_file1 = get_words(file1)
          words_file2 = get_words(file2)

          common_words = sorted(words_file1 & words_file2)

          if args.outfile:
              with open(args.outfile, 'w') as out_file:
                  for word in common_words:
                      out_file.write(f"{word}\n")
          else:
              for word in common_words:
                  print(word)

  except IOError as e:
      print(f"common.py: error: {e}")
      sys.exit(1) 

# --------------------------------------------------
if __name__ == '__main__':
    main()
