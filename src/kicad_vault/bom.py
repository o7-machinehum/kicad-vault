import os
import xmltodict
import digikey
from digikey.v3.productinformation import KeywordSearchRequest
import pdb

# Import the KiCad python helper module and the csv formatter
import csv
import sys

if sys.platform.startswith("linux"):
    sys.path.append('/usr/share/kicad/plugins/')
    KICAD_CLI = 'kicad-cli'
elif sys.platform == "darwin":
    sys.path.append('/Applications/KiCad/KiCad.app/Contents/SharedSupport/plugins/')
    sys.path.append(os.path.expanduser('~/Documents/KiCad/6.0/scripting/plugins'))
    KICAD_CLI = '/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli'
else:
    KICAD_CLI = 'kicad-cli'

import kicad_netlist_reader

def generate_csv(prj, output, part_num):
    os.system(f"{KICAD_CLI} sch export python-bom {prj} --output bom.xml")
    os.environ['DIGIKEY_STORAGE_PATH'] = '.'

    # Generate an instance of a generic netlist, and load the netlist tree from
    # the command line option. If the file doesn't exist, execution will stop
    net = kicad_netlist_reader.netlist("bom.xml")

    # Open a file to write to, if the file cannot be opened output to stdout
    # instead
    try:
        f = open(f"{output}", 'w')
    except IOError:
        e = "Can't open output file for writing: " + f"{output}"
        print(__file__, ":", e, sys.stderr)
        f = sys.stdout

    # Create a new csv writer object to use as the output formatter
    out = csv.writer(f, lineterminator='\n', delimiter=',', quotechar='\"', quoting=csv.QUOTE_ALL)

    # Which prices are you interested in
    price_brackets = {1:"", 10:"", 100:"", 500:"", 1000:""}
    header = ["Ref", "Qnty", "Value", "Footprint", "Part Number",
        "Detailed Description", "QTD Available"]

    for i in list(price_brackets.keys()):
        header.append(f"Price (QTD {i})")

    # Output a set of rows for a header providing general information
    out.writerow(["Source:", net.getSource()])
    out.writerow(["Date:", net.getDate()])
    out.writerow(["Tool:", net.getTool()])
    out.writerow(["Generator:", sys.argv[0]])
    out.writerow(["Component Count:", len(net.components)])
    out.writerow(header)

    # Get all of the components in groups of matching parts + values
    # (see ky_generic_netlist_reader.py)
    grouped = net.groupComponents()

    # Output all of the component information
    for group in grouped:
        refs = ""

        # Add the reference of every component in the group and keep a reference
        # to the component so that the other data can be filled in once per group
        for component in group:
            refs += component.getRef() + ", "
            c = component

        row = [refs, len(group), c.getValue(), c.getFootprint(), c.getField(part_num)]

        try:
            part = digikey.product_details(c.getField(part_num))
            for part_prices in part.standard_pricing:
                if part_prices.break_quantity in price_brackets:
                    price_brackets[part_prices.break_quantity] = part_prices.unit_price

            row.extend([part.detailed_description, part.quantity_available])
            row.extend(list(price_brackets.values()))
        except (ValueError, AttributeError):
            print(f"{refs}: No Part Number")

        # Fill in the component groups common data
        out.writerow(row)

    os.remove("bom.xml")

if __name__ == "__main__":
    generate_csv("../ovrdrive/ee/ovrdrive/ovrdrive.kicad_sch",
        "http/boms/ovrdrive.csv", "MPN")
