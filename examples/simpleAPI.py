"""
A simple example script demonstrating how to build peptide by PCcli.seq2pep.

The script generates a peptide of "AKlsDe" in alpha-helix conformation, and it stores the peptide under the name "simpleAPI.pdb".
"""

import Bio.PDB
from PeptideConstructor.PCcli import seq2pep

## create peptide by seq2pep function

## initialize the sequence
sequence = "AKlsDe"

## seq2pep need 3 parameters:
##     - sequence : the sequence of peptide
##     - capping  : 0 for no cappings, default
##                  1 for cappings
##                  3 for adding ACE at N terminal
##                  4 for adding NME at C terminal
##     - ss       : secondary structure
##                  l for linear peptide, default
##                  a for alpha helix
##                  b for beta sheet
##                  la for left hand helix
##                  lb for mirror inverted beta sheet
## seq2pep returns two variable:
##     - peptide structure
##     - sequence in list format
structure, seq = seq2pep(sequence, 0, "a")

## if you do not need to assign secondary structure,
## you can use seq2pep in a simple way which produce a linear peptide
structure, seq = seq2pep(sequence)

## save structure to pdb file
out = Bio.PDB.PDBIO()
out.set_structure(structure)
out.save("simpleAPI.pdb")
