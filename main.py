import bom

prj = "/home/machinehum/projects/id01/ee/trackpad_pcb_cs/trackpad.kicad_sch --output bom.xml"
part_num = "MPN"
bom.generate_csv(prj, part_num)
