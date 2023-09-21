import sys
from . import bom

def main():
    bom_name = sys.argv[1].split(".")[0] + ".csv"
    bom.generate_csv(f"{sys.argv[1]}", bom_name, "MPN")

if __name__ == "__main__":
    main()
