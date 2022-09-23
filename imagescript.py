#! /usr/bin/env python3
import os, sys
from PIL import Image

input_folder = "scans/"
output_folder = "pdf/"

for infile in os.listdir(input_folder):
    print(infile)
    outfile = os.path.splitext(infile)[0]

    with Image.open(f'{input_folder}{infile}').convert('RGB') as im:
        width, height = im.size
        print(im.size)
        height = int(height/(width/1400))
        new =im.resize((1400, height))
        print(new.size)
        new.save(output_folder + outfile + ".pdf", "PDF")
        print('succes')
