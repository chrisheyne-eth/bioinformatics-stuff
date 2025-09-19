from Bio import SeqIO

def trim_fasta(input_file, output_file, start=0, end=None):
    """
    Trims all sequences from start to end.
    Args:
        input_file (str): Path to the input FASTA file.
        output_file (str): Path to the output FASTA file.
        start (int): Start position for trimming (0-based).
        end (int or None): End position for trimming. If None, trims to the end of the sequence.
    """
    with open(output_file, "w") as out:
        for record in SeqIO.parse(input_file, "fasta"):
            trimmed_seq = record.seq[start:end] # Slice
            record.seq = trimmed_seq
            SeqIO.write(record, out, "fasta")