#!/usr/bin/env python3
"""tests for get_start_codon_positions.py"""

import os

prg = './get_start_codon_positions.py'

# --------------------------------------------------
def test_get_start_codon_positions() -> None:
    """ Test create_codons """

    assert get_start_codon_positions('GGGGGGG') == []
    assert get_start_codon_positions('ATGG') == [0]
    assert get_start_codon_positions('GGGGGATG') == [5]
    assert get_start_codon_positions('ATGCCATGATG') == [0, 5, 8]
    assert get_start_codon_positions('atgatgatg') == [0, 3, 6]
    assert get_start_codon_positions('atTGGtgatg') == [7]
