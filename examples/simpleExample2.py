"""
A simple example script demonstrating how to build peptide by PeptideConstructor in primitive way.

The script generates a peptide of "AKlsDe" in self-defined conformation, and it stores the peptide under the name "simple_example.pdb".
"""

import Bio.PDB
from PeptideConstructor import Geometry
from PeptideConstructor import PeptideBuilder


## create a peptide of "AKlsDe", uppercases mean L amino acids while lowercases indicate D amino acids

## construct the first amino acid
geo = Geometry.geometry("A")
## delete the next two lines to not assign secondary structure
geo.phi = -60
geo.psi_im1 = -50
structure = PeptideBuilder.initialize_res(geo)

## construcet the rest
geo = Geometry.geometry("K")
PeptideBuilder.add_residue(structure, geo)
geo = Geometry.geometry("l")
PeptideBuilder.add_residue(structure, geo)
geo = Geometry.geometry("s")
PeptideBuilder.add_residue(structure, geo)
geo = Geometry.geometry("D")
PeptideBuilder.add_residue(structure, geo)
geo = Geometry.geometry("e")
PeptideBuilder.add_residue(structure, geo)

## add terminal oxygen (OXT) to the final amino acid
## if "NME" capping has been added, NO OXT should be added.
PeptideBuilder.add_terminal_OXT(structure)

## save peptide structure to a pdb file
out = Bio.PDB.PDBIO()
out.set_structure(structure)
out.save("simpleExample.pdb")
