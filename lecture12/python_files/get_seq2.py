#!/usr/bin/env python3

#the second sequence file
import os
import subprocess
os.chdir("../lecture12/resources/")
#obtain the fasta file using esearch and acc number
subprocess.call("esearch -db nucleotide -query AJ223353 | efetch -format fasta > './seq2.fasta'", shell=True)
#obtain the annotation of this sequence
subprocess.call("esearch -db nucleotide -query AJ223353 | efetch -format gff > './annotation.gff'", shell=True)
#find the CDS from annotation file
#CDS show the start and end numebr of coding region
with open("./annotation.gff",mode="r") as f:
    lines = f.readlines()
    for line in lines:
        if line.find("CDS") != -1:
            coding_region=line
#result: CDS        start_number..end_number
#we need to obtain the start and end nunber seperately
positions = coding_region.split("S")[-1].strip()
positions = positions.split("..")
start_point = int(positions[0])
end_point = int(positions[1])

#send the start and end point to outside
print("{} {}".format(start_point, end_point))
