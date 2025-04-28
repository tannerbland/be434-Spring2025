#!/usr/bin/env python3
"""
Author : Tanner Bland <tannerbland@arizona.edu>
Date   : 2025-03-24
Purpose: Generate synthetic DNA/RNA sequences
"""

import argparse
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create synthetic DNA/RNA sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o', '--outfile', 
                        help='Output filename (default: out.fa)', 
                        metavar='str', 
                        type=str, 
                        default='out.fa')

    parser.add_argument('-t', '--seqtype', 
                        help='Sequence type: "dna" or "rna" (default: dna)', 
                        metavar='str', 
                        type=str, 
                        choices=['dna', 'rna'], 
                        default='dna')

    parser.add_argument('-n', '--numseqs', 
                        help='Number of sequences to create (default: 10)', 
                        metavar='int', 
                        type=int, 
                        default=10)

    parser.add_argument('-m', '--minlen', 
                        help='Minimum length (default: 50)', 
                        metavar='int', 
                        type=int, 
                        default=50)

    parser.add_argument('-x', '--maxlen', 
                        help='Maximum length (default: 75)', 
                        metavar='int', 
                        type=int, 
                        default=75)

    parser.add_argument('-p', '--pctgc', 
                        help='Percentage of GC content (0 to 1, default: 0.5)', 
                        metavar='float', 
                        type=float, 
                        default=0.5)

    parser.add_argument('-s', '--seed', 
                        help='Random seed', 
                        metavar='int', 
                        type=int, 
                        default=None)

    args = parser.parse_args()

    # Check if pctgc is within the valid range [0, 1]
    if not 0 <= args.pctgc <= 1:
        parser.error(f'--pctgc "{args.pctgc}" must be between 0 and 1')

    return args

# --------------------------------------------------
def create_pool(pctgc, max_len, seq_type):
    """ Create the pool of bases """
    if seq_type == 'dna':
        t_or_u = 'T'
    else:
        t_or_u = 'U'
    num_gc = int((pctgc / 2) * max_len)
    num_at = int(((1 - pctgc) / 2) * max_len)
    pool = 'A' * num_at + 'C' * num_gc + 'G' * num_gc + t_or_u * num_at

    for _ in range(max_len - len(pool)):
        pool += random.choice(pool)

    return ''.join(sorted(pool))

# --------------------------------------------------
def gc_fraction(seq, ambiguous="remove"):
    "Calculate GC content of a sequence; taken directly from Bio.SeqUtils gc_fraction()."
    if ambiguous not in ("weighted", "remove", "ignore"):
        raise ValueError(f"ambiguous value '{ambiguous}' not recognized")

    gc = sum(seq.count(x) for x in "CGScgs")

    if ambiguous == "remove":
        length = gc + sum(seq.count(x) for x in "ATWUatwu")
    else:
        length = len(seq)

    if ambiguous == "weighted":
        gc += sum(
            (seq.count(x) + seq.count(x.lower())) * _gc_values[x] for x in "BDHKMNRVXY"
        )

    if length == 0:
        return 0

    return gc / length * 100

# --------------------------------------------------
def main():
    """Generate synthetic DNA/RNA sequences"""

    args = get_args()
    random.seed(args.seed)
    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)

    with open(args.outfile, 'w') as outfile:
        for i in range(1, args.numseqs + 1):
            seq_len = random.randint(args.minlen, args.maxlen)
            seq = ''.join(random.sample(pool, seq_len))
            gc_content = gc_fraction(seq)
            outfile.write(f'>Sequence_{i}\n{seq}\n')

    print(f'Done, wrote {args.numseqs} {args.seqtype.upper()} sequences to "{args.outfile}".')

# --------------------------------------------------
if __name__ == '__main__':
    main()
