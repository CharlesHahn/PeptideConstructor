## author : charlie
## date : 20211214DR

import argparse
import Bio.PDB
import Geometry
import PeptideBuilder


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
        choices=["a", "b", "l"],
        help="second structure. l : line, default; a : alpha helix; b : beta sheet. ",
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

    ## generate peptide
    geo = Geometry.geometry(sequence[0])
    if args.ss == "a":
        geo.phi = -60
        geo.psi_im1 = -40
    elif args.ss == "b":
        geo.phi = -140
        geo.psi_im1 = 130
    pep = PeptideBuilder.initialize_res(geo)
    for aa in sequence[1:]:
        geo = Geometry.geometry(aa)
        if args.ss == "a":
            geo.phi = -60
            geo.psi_im1 = -40
        elif args.ss == "b":
            geo.phi = -140
            geo.psi_im1 = 130
        PeptideBuilder.add_residue(pep, geo)
    if args.cap == 0 or args.cap == 2:
        PeptideBuilder.add_terminal_OXT(pep)

    out = Bio.PDB.PDBIO()
    out.set_structure(pep)
    out.save(args.o)

    print('"=== May you good day ! ==="')


if __name__ == "__main__":
    main()
