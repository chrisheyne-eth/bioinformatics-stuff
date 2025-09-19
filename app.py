import streamlit as st

st.set_page_config(page_title="Chris' Bioinformatics Dashboard")

st.title("Chris' Bioinformatics Dashboard")

st.write("""
Welcome to your Bioinformatics toolkit!  
Use the sidebar to navigate between tools.
""")

st.subheader("Available Tools:")
st.markdown("""
- ✂️ **FASTA Trimmer** — trim sequences from FASTA files  
- 📏 **Length Filter** — filter sequences by length  
- 🌱 **GC Content Filter** — filter sequences by GC content  
- 📊 **Stats Report** — get stats like sequence count, GC%, and N50
""")