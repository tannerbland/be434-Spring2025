#!/usr/bin/env python3
"""
Purpose: Filter delimited records based on a value that may appear in a specific column.
Author: Tanner Bland <tannerbland@arizona.edu>
"""

import argparse
import csv
import re
import sys

def main():
    """Main function to handle command-line arguments and filtering logic."""
    parser = argparse.ArgumentParser(description='Filter delimited records')

    # Required arguments
    parser.add_argument('-f', '--file', 
                        required=True, 
                        type=argparse.FileType('r'), 
                        help='Input file (default: None)')
    parser.add_argument('-v', '--val', 
                        required=True, 
                        help='Value for filter (default: None)')

    # Optional arguments
    parser.add_argument('-c', '--col', 
                        default='', 
                        help='Column name for filter (default: )')
    parser.add_argument('-o', '--outfile', 
                        default='out.csv', 
                        type=argparse.FileType('w'), 
                        help='Output filename (default: out.csv)')
    parser.add_argument('-d', '--delimiter', 
                        default=',', 
                        help='Input delimiter (default: ,)')

    args = parser.parse_args()

    # Create CSV reader
    reader = csv.DictReader(args.file, delimiter=args.delimiter)

    # Validate column name if provided
    if args.col and args.col not in reader.fieldnames:
        print(f'--col "{args.col}" not a valid column!', file=sys.stderr)
        print(f'Choose from {", ".join(reader.fieldnames)}', file=sys.stderr)
        sys.exit(1)

    # Create CSV writer
    writer = csv.DictWriter(args.outfile, fieldnames=reader.fieldnames)
    writer.writeheader()

    # Compile regex pattern for case-insensitive search
    pattern = re.compile(re.escape(args.val), re.IGNORECASE)
    match_count = 0

    for record in reader:
        if args.col:
            # Search in specific column
            if pattern.search(str(record[args.col])):
                writer.writerow(record)
                match_count += 1
        else:
            # Search in all columns
            for value in record.values():
                if pattern.search(str(value)):
                    writer.writerow(record)
                    match_count += 1
                    break

    # Close files
    args.file.close()
    args.outfile.close()

    print(f'Done, wrote {match_count} to "{args.outfile.name}".')

if __name__ == '__main__':
    main()