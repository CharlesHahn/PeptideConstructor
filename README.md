# DL-PeptideBuilder: A simple Python library to generate model (DL-)peptides.

## Still working on this:

- [x] add D amino acids support
- [x] add command-line interface support
- [ ] add support of more amino acids
- [ ] add support of adding amino acids to existing protein
- [ ] add energy minimization or conformation optimization support
- [ ] further more, add DNA/RNA support

## Installation

You can install PeptideConstructor with pip:

```
pip install PeptideConstructor
```

PeptideBuilder has two required dependency: 
- Biopython for PDB IO.
- Numpy for coordinates calculation.

## Usage

After installation, `PCcli` command could be called in your terminal. `PCcli` could generage peptide PDB file from sequence in a simple way.

For instance:

```
PCcli -s AaDdKSQym -o test.pdb
```
which will generage a test.pdb file in current directory which contains a peptide with sequence of `AaDdKSQym`, in which, uppercase indicates L amino acids and lowercase indicates D amino acids. 

Also, secondary structure and capping of peptide could be applied through `PCcli`.

Sure you could generage peptide in original way by writing codes. see [PeptideBuilder](https://github.com/clauswilke/PeptideBuilder) for more infomation.


## Post-processing Tools Recommandation:

1. add hydrogens : reduce, TINKER
2. structure optimization: ModRefiner, TINKER/minimize

## Others

This repo is based on [Lun4m/PeptideBuilder.git](https://github.com/Lun4m/PeptideBuilder) and [clauswilke/PeptideBuilder.git](https://github.com/clauswilke/PeptideBuilder). Cite their original paper.

**Reference:**
M. Z. Tien, D. K. Sydykova, A. G. Meyer, C. O. Wilke (2013). PeptideBuilder:
A simple Python library to generate model peptides. PeerJ 1:e80.
