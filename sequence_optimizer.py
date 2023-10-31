#this function takes protein amino acid sequence from the uniprot database as an input, and outputs an optimized sequence with kozak sequence, and optimized GC content

#set up varibles and dependencies

from Bio.Data import CodonTable
from Bio.Seq import Seq
fasta_file = 'P03969.fasta'
sequence = ''

#open the file and remove the header
with open(fasta_file, 'r') as fasta:  
    for idx, line in enumerate(fasta):
        if idx > 0:
            sequence = sequence + line.strip()
print(sequence)

aaseq = Seq(sequence)
table = CodonTable.unambiguous_dna_by_id[1]

# Create a dictionary mapping each amino acid to the first codon encoding it
aa_to_codon = {}
for codon, aa in table.forward_table.items():
    if aa not in aa_to_codon:
        aa_to_codon[aa] = codon



#convert amino acid sequence to nucleotides
nucleotide_seq_str = ''.join([aa_to_codon[aa] for aa in aaseq])
print("Nucleotide sequence:", nucleotide_seq_str)
