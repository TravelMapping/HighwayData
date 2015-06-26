#!/usr/bin/env python3
# Travel Mapping Project, Jim Teresco, 2015
"""Python code to read an old-format .wpt file and 
write a new format .wpt2 file.

The old format consists of lines such as

PA/NY +0 http://www.openstreetmap.org/?lat=42.252473&lon=-79.761515

which would convert to 

42.252473 79.761515 PA/NY +0

(c) 2015, Jim Teresco
"""

import argparse

# argument parsing
parser = argparse.ArgumentParser(description="Convert wpt to wpt2 file.")
parser.add_argument("fileroot", help="root file name to be converted (fileroot.wpt becomes fileroot.wpt2)")
args = parser.parse_args()
outfile = open(args.fileroot+'.wpt2','wt')
with open(args.fileroot+'.wpt','rt') as infile:
    lines = infile.readlines()

for line in lines:
    parts = line.split()
    url_parts = parts[-1].split('=')
    lat_string = url_parts[1].split("&")[0] # chop off "&lon"
    lng_string = url_parts[2].split("&")[0] # chop off possible "&zoom"
    outfile.write(lat_string + ' ' + lng_string + ' ' + parts[0])
    for p in parts[1:-1]:
        outfile.write(' ' + p)
    outfile.write('\n')

outfile.close()
