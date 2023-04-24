import bom
import pdb
from pathlib import Path
import os
from http.server import HTTPServer, CGIHTTPRequestHandler
import html_gen

part_num = "MPN"
srv = "http"

try:
    os.mkdir(srv)
    os.mkdir(f"{srv}/boms")
except(FileExistsError):
    pass


files = []
try:
    f = open(f"{srv}/prj.txt", "r")
    files = f.read().split("\n")
except(FileNotFoundError):
    for path in Path('../').rglob('*.kicad_sch'):
        k = input(f"{str(path)} Add this project? (Y/n): ")
        if k == "y" or k == "Y":
            files.append(str(path))
    f = open(f"{srv}/prj.txt", "w")
    for i in files:
        f.write(f"{i}\n")
    f.close()

# Create index.html and all bom files
files = dict.fromkeys(files)
with open(f"{srv}/index.html", "w") as f:
    # Create links
    for file in files:
        k = file.split("/")[-1].split(".")[0]
        files[file] = {"html": f"boms/{k}.html", "csv": f"boms/{k}.csv"}
        f.write(f'<a href="{files[file]["html"]}">{file}</a><br>\n')
        bom.generate_csv(f"{file}", srv + "/" + files[file]["csv"], part_num)
        html_gen.csv_to_html(srv + "/" + files[file]["csv"],
            srv + "/" + files[file]["html"])


# os.chdir('http')
# server_object = HTTPServer(server_address=('', 3000), RequestHandlerClass=CGIHTTPRequestHandler)
# server_object.serve_forever()
