def read_dna(dna_file_name):
    """Reads and returns the input sequence with special characters removed"""
    
    # Using the with statement here closes the file automatically!
    with open(dna_file_name, "r") as dna_file:
        dna_sequence = dna_file.read()

    return dna_sequence.replace("\n", "").replace("\r", "")

def translate_dna(dna_sequence):
    """Translated a DNA sequence into a protein sequence"""
      
    translation_table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

    dna_sequence_length = len(dna_sequence)

    if dna_sequence_length % 3 != 0:
        return ""

    protein_sequence = ""

    for i in range(0, dna_sequence_length, 3):
        code = dna_sequence[i : i+3]
        protein_sequence += translation_table[code]
    
    return protein_sequence

dna_file_name = "C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 3/DNA Translating/DNA.txt"
dna_sequence = read_dna(dna_file_name)

protein_file_name = "C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 3/DNA Translating/protein.txt"
protein_sequence = read_dna(protein_file_name)

print(protein_sequence == translate_dna(dna_sequence[20:935]))