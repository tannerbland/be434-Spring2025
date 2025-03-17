#!/usr/bin/env python3
"""
Author : Tanner Bland <tannerbland@arizona.edu>
Date   : 2025-03-17
Purpose: Transcribe DNA into RNA
"""

import argparse
import os
import sys
import shutil

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Transcribe DNA into RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        nargs='+',
                        help='Input DNA file')

    parser.add_argument('-o',
                        '--outdir',
                        metavar='DIR',
                        help='Output directory',
                        type=str,
                        default='out')

    args = parser.parse_args()

    # Check if input files exist
    missing_files = [file for file in args.files if not os.path.isfile(file)]
    if missing_files:
        parser.error(f"No such file or directory: '{missing_files[0]}'")

    return args

# --------------------------------------------------
def transcribe_dna_to_rna(dna_sequence):
    """Convert DNA sequence to RNA by replacing 'T' with 'U'."""
    return dna_sequence.replace('T', 'U')

# --------------------------------------------------
def process_files(input_files, output_dir):
    """Process input files, transcribing DNA to RNA and writing to output files."""
    os.makedirs(output_dir, exist_ok=True)
    count_sequences = 0
    count_files = len(input_files)

    for file_path in input_files:
        with open(file_path, 'r') as infile:
            dna_sequence = infile.read().strip()

        # Split the file into separate sequences (assuming sequences are separated by newline)
        sequences = dna_sequence.split('\n')
        rna_sequences = [transcribe_dna_to_rna(seq) for seq in sequences]

        # Write all RNA sequences to the file
        output_file_path = os.path.join(output_dir, os.path.basename(file_path))
        with open(output_file_path, 'w') as outfile:
            outfile.write('\n'.join(rna_sequences) + '\n')

        count_sequences += len(sequences)

    seq_word = "sequence" if count_sequences == 1 else "sequences"
    file_word = "file" if count_files == 1 else "files"

    print(f"Done, wrote {count_sequences} {seq_word} in {count_files} {file_word} to directory \"{output_dir}\".")

# --------------------------------------------------
def main():
    """Main function"""
    args = get_args()
    process_files(args.files, args.outdir)

# --------------------------------------------------
if __name__ == '__main__':
    main()
