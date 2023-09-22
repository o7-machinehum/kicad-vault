import argparse
import sys
from . import bom

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("fname", help="KiCad file name you want to create a BOM for")
    parser.add_argument("--field", help="Part field inside of KiCad ie: MPN")
    args = parser.parse_args()

    bom_name = args.fname.split(".")[0] + ".csv"

    if args.field != None:
        bom.generate_csv(args.fname, bom_name, args.field)
    else:
        bom.generate_csv(args.fname, bom_name, "MPN")

if __name__ == "__main__":
    main()
