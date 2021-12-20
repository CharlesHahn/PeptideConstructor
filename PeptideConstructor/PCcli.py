"""This module is part of the PeptideConstructor library, written by CharlesHahn. This pacage is based on Lun4m/PeptideBuilder.git and clauswilke/PeptideBuilder.git. 

This PCcli module allows you to create (DL-) peptide with different secondary structures in a simple way. And obviously, it's a CLI program.

This file is provided to you under the MIT License."""

import time
import argparse
from typing import Tuple
import Bio.PDB
from Bio.PDB.Structure import Structure

# import Geometry
# import PeptideBuilder
from PeptideConstructor import Geometry, PeptideBuilder


def seq2pep(sequence: str, cap: int = 0, ss: str = "l") -> Tuple[Structure, list]:
    """
    An simple function to convert sequence into 3D peptide

    - sequence : peptide sequence. one letter represent an amino acid. Uppercase is L amino acids and lowercase is D amino acid.

    - cap : whether to add capping
            0 : default, no capping
            1 : capping
            2 : only add ACE capping to the beginning
            3 : only add NME capping to the end

    - ss : apply secondary structure
            l : default, linear
            a : alpha helix
            b : beta sheet
            la : left hand helix
            lb : mirror inverted beta sheet.

    return : pep : a peptide structure (class of Biopython); seq : list of AA
    """

    ## deal with the sequence
    seq = [sequence[i] for i in range(len(sequence))]
    if cap == 1:
        seq = ["ACE"] + seq + ["NME"]
    elif cap == 2:
        seq = ["ACE"] + seq
    elif cap == 3:
        seq = seq + ["NME"]
    # print(sequence)

    ## generate geometry for each AA
    geo_list = []
    for a_i in range(len(seq)):
        geo = Geometry.geometry(seq[a_i])

        ## apply secondary structure
        if ss == "a":
            geo.phi = -60
            geo.psi_im1 = -50
        elif ss == "la":
            geo.phi = 60
            geo.psi_im1 = 50
        elif ss == "b":
            geo.phi = -140
            geo.psi_im1 = 130
        elif ss == "lb":
            geo.phi = 140
            geo.psi_im1 = -130

        geo_list.append(geo)

    ## reminds about Proline
    if (ss == "a" or ss == "la") and ("P" in seq or "p" in seq):
        print(
            "\n=== Warning : Appling Alpha Helix to Proline or D-Proline may cause coordinates conflicts. Structure Repair or Energy Minimization may be needed ! ===\n"
        )

    ## generate peptide structure
    pep = PeptideBuilder.initialize_res(geo_list[0])
    for geo_i in range(1, len(geo_list)):
        PeptideBuilder.add_residue(pep, geo_list[geo_i])

    ## add OXT if needed
    if cap == 0 or cap == 2:
        PeptideBuilder.add_terminal_OXT(pep)

    return pep, seq


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        required=True,
        help="the sequence of peptide. Uppercase for L amino acid, lowercase for D amino acid. eg. KlvAfFk",
    )
    parser.add_argument("-o", required=True, help="output pdb file")
    parser.add_argument(
        "-cap",
        default=0,
        type=int,
        choices=[0, 1, 2, 3],
        help="whether to add capping. 0: default, no capping, 1 : capping, 2: only add ACE at N terminal, 3 : only add NME at C terminal.",
    )
    parser.add_argument(
        "-ss",
        default="l",
        choices=["a", "b", "l", "la", "lb"],
        help="second structure. l : line, default; a : alpha helix; b : beta sheet; la : left hand helix; lb : mirror inverted beta sheet. ",
    )
    args = parser.parse_args()

    ## convert sequence to peptide
    pep, seq = seq2pep(args.s, args.cap, args.ss)

    ## write peptide structure to pdb file
    out = Bio.PDB.PDBIO()
    out.set_structure(pep)
    out.save(args.o)

    ## add sequence infomation into pdb file
    with open(args.o, "r") as fo:
        pdb_content = fo.read()
    with open(args.o, "w") as fo:
        fo.write(
            "USER  Sequence : {} \n".format(
                "-".join([str(i + 1) + seq[i] for i in range(len(seq))])
            )
        )
        fo.write("USER  generated at {} \n".format(time.strftime("%Y-%m-%d %H:%m:%S")))
        fo.write(pdb_content)

    ## print ending message
    print(
        " ==> Peptide {} has been generated and saved in {} in current directory. \n ==> May you good day !".format(
            "-".join([str(i + 1) + seq[i] for i in range(len(seq))]), args.o
        )
    )


if __name__ == "__main__":
    main()
