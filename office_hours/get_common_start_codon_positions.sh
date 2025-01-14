#!/usr/bin/env python3

from typing import Dict, List, NamedTuple, TextIO

def main():
    """Find start codon"""

    kmer_positions1 = get_start_codon_positions('ATGGGGG')
    kmer_positions2 = get_start_codon_positions('ATGGGGGGG')

    for common in set(kmer_positions1).intersection(set(kmer_positions2)):
        print("common:", common)



# --------------------------------------------------
def get_start_codon_positions(seq: str) -> List[int]:
    """ Find start codon positions in a sequence """

    start_codon = "ATG"
    k = 3 # codon size
    n = len(seq) - k + 1
    start_codon_positions = []
    seq = seq.upper()
   
    for i in range(n):
        codon = seq[i:i + k]
        if codon == start_codon:
            start_codon_positions.append(i)
    return start_codon_positions

# --------------------------------------------------
def test_get_start_codon_positions() -> None:
    """ Test create_codons """

    assert get_start_codon_positions('GGGGGGG') == []
    assert get_start_codon_positions('ATGG') == [0]
    assert get_start_codon_positions('GGGGGATG') == [5]
    assert get_start_codon_positions('ATGCCATGATG') == [0, 5, 8]
    assert get_start_codon_positions('atgatgatg') == [0, 3, 6]
    assert get_start_codon_positions('atTGGtgatg') == [7]

# --------------------------------------------------
if __name__ == '__main__':
    main()

