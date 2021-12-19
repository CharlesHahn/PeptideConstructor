## author : charlie
## date : 20211214DR

import Bio.PDB
from PeptideConstructor import Geometry, PeptideBuilder

# import Geometry
# import PeptideBuilder


geo = Geometry.geometry("D")
# geo.phi = -60
# geo.psi_im1 = -40
# geo.phi = -140
# geo.psi_im1 = 130
pep = PeptideBuilder.initialize_res(geo)

for aa in "lvAfFK":
    geo = Geometry.geometry(aa)
    # geo.phi = -60
    # geo.psi_im1 = -40
    # geo.phi = -140
    # geo_psi_im1 = 130
    PeptideBuilder.add_residue(pep, geo)

# geo = Geometry.geometry("NME")
# PeptideBuilder.add_residue(pep, geo)
PeptideBuilder.add_terminal_OXT(pep)

out = Bio.PDB.PDBIO()
out.set_structure(pep)
out.save("test2.pdb")
