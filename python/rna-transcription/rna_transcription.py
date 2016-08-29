rna_seq = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
}


def to_rna(dna_seq):
    return ''.join(rna_seq[rna] for rna in dna_seq)
