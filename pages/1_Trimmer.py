import streamlit as st
from Bio import SeqIO
from pages.fasta_utils import trim_fasta

st.title("✂️ FASTA Trimmer")

# File upload
uploaded_file = st.file_uploader("Upload a FASTA file", type=["fasta", "fa"])

if uploaded_file:
    st.write("File uploaded: ", uploaded_file.name)
    # Trimming parameters
    start = st.number_input("Start position", min_value=0, value=0)
    end = st.number_input("End position", min_value=0, value=100)
    if end == 0:
        end = None  # If end is 0, treat it as None (to the end of the sequence)

    if st.button("Trim FASTA"):
        output_file = "data/trimmed_" + uploaded_file.name
        trim_fasta(uploaded_file, output_file, start, end)
        st.success(f"FASTA file trimmed successfully! Saved in {output_file}")
        with open(output_file, "rb") as f:
            st.text(f.read())