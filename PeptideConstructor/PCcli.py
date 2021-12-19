"""This module is part of the PeptideConstructor library, written by CharlesHahn. This pacage is based on Lun4m/PeptideBuilder.git and clauswilke/PeptideBuilder.git. 

This PCcli module allows you to create (DL-) peptide with different secondary structures in a simple way. And obviously, it's a CLI program.

This file is provided to you under the MIT License."""

import argparse
import Bio.PDB

# import Geometry
# import PeptideBuilder
from PeptideConstructor import Geometry, PeptideBuilder


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

    ## deal with sequence
    sequence = [args.s[i] for i in range(len(args.s))]
    if args.cap == 1:
        sequence = ["ACE"] + sequence + ["NME"]
    elif args.cap == 2:
        sequence = ["ACE"] + sequence
    elif args.cap == 3:
        sequence = sequence + ["NME"]
    # print(sequence)

    ## generate geometry for each AA
    geo_list = []
    for a_i in range(len(sequence)):
        geo = Geometry.geometry(sequence[a_i])

        if args.ss == "a":
            geo.phi = -60
            geo.psi_im1 = -50
        elif args.ss == "la":
            geo.phi = 60
            geo.psi_im1 = 50
        elif args.ss == "b":
            geo.phi = -140
            geo.psi_im1 = 130
        elif args.ss == "lb":
            geo.phi = 140
            geo.psi_im1 = -130

        geo_list.append(geo)

    ## reminds about Proline
    if (args.ss == "a" or args.ss == "la") and ("P" in sequence or "p" in sequence):
        print(
            "\n=== Warning : Appling Alpha Helix to Proline or D-Proline may cause coordinates conflicts. Structure Repair or Energy Minimization may be needed ! ===\n"
        )

    ## generate peptide
    pep = PeptideBuilder.initialize_res(geo_list[0])
    for geo_i in range(1, len(geo_list)):
        PeptideBuilder.add_residue(pep, geo_list[geo_i])

    ## add OXT if needed
    if args.cap == 0 or args.cap == 2:
        PeptideBuilder.add_terminal_OXT(pep)

    ## generate pdb file
    out = Bio.PDB.PDBIO()
    out.set_structure(pep)
    out.save(args.o)

    with open(args.o, "r") as fo:
        pdb_content = fo.read()

    with open(args.o, "w") as fo:
        fo.write(
            "USER  Sequence : {} \n".format(
                "-".join([str(i + 1) + sequence[i] for i in range(len(sequence))])
            )
        )
        fo.write(pdb_content)

    print(
        " ==> Peptide {} has been generated and saved in {} in current directory. \n ==> May you good day !".format(
            "-".join([str(i + 1) + sequence[i] for i in range(len(sequence))]), args.o
        )
    )


if __name__ == "__main__":
    main()
