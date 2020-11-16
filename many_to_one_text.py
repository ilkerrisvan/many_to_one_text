import glob
import sys

loc_texts = sys.argv[1] ## location of texts
loc_output_text = sys.argv[2] 

read_files = glob.glob(f"{loc_texts}/*.txt")

with open(loc_output_text, "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
