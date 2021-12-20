"""
A simple example script demonstrating how to build peptide by PeptideConstructor.

The script generates a peptide of "AKlsDe" in alpha-helix conformation, and it stores the peptide under the name "simple_example.pdb".
"""

import Bio.PDB
from PeptideConstructor import Geometry
from PeptideConstructor import PeptideBuilder

## create a peptide of "AKlsDe", uppercases mean L amino acids while lowercases indicate D amino acids

## initial the sequence
seq = ["A", "K", "l", "s", "D", "e"]
## with cappings
# seq = ["ACE", "A", "K", "l", "s", "D", "e", "NME"]

## assign the topologies of each amino acid
geo_list = []
for aa in seq:
    ## get the default geometry of each amino acid
    geo = Geometry.geometry(aa)
    ## if you want to set secondary structure, change phi and psi_im1
    geo.phi = -60
    geo.psi_im1 = -40
    geo_list.append(geo)

## create peptide from geo_list
## you need to initialize the fist residue of each peptide
structure = PeptideBuilder.initialize_res(geo_list[0])
for geo in geo_list[1:]:
    PeptideBuilder.add_residue(structure, geo)

## add terminal oxygen (OXT) to the final amino acid
## if "NME" capping has been added, NO OXT should be added.
PeptideBuilder.add_terminal_OXT(structure)

## save peptide structure to a pdb file
out = Bio.PDB.PDBIO()
out.set_structure(structure)
out.save("simpleExample.pdb")
