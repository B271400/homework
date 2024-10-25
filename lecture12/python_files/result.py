#!/usr/bin/python3
import os
import subprocess
import shutil
import sys

#parameters from outside
file_path = sys.argv[1]
start_point = int(sys.argv[2])
end_point = int(sys.argv[3])
exon_number = int(sys.argv[4])
question_number = int(sys.argv[5])

os.chdir("../lecture12/")
#remove the header of fasta file, remove the \n of each line
header_line = ""
with open(file_path, mode="r") as f:
    lines = f.readlines()
    #create a str to join all the lines
    seq_str = ""
    for line in lines:
        if line.find(">") == -1:
            #remove the \n at each line
            seq_str += line.strip()
        else:
            #save the header line
            header_line = line.strip()

#write the fasta file without header
with open("resources/no_header{}.fasta".format(question_number), mode="w") as f:
    new_str = ""
    #set all the characters into uppercase
    for s in seq_str:
        if s in ("A","T","C","G","R","r","a","t","c","g"):
            s = s.upper()
            new_str+=s
    f.write(new_str)

#sepeate the file to 2 files, 1 with non-coding sequence, 1 with coding sequence
with open("resources/no_header{}.fasta".format(question_number), mode="r") as f:
    result = f.read()
    frag1 = result[:start_point-1]
    frag2 = result[start_point-1:end_point]
    frag3 = result[end_point:]

#a function to create files with header line 
def add_seq_to_file(seq, type, seq_number=""):
    with open("resources/{}{}_{}.fasta".format(type,seq_number, question_number), mode="w") as f:
        if header_line:
            f.write(header_line + " the {} region, length of this sequence is {} \n".format(type, len(seq)))
            f.write(seq)
        else:
            #if no header line before, create your own header line
            f.write("> this is the {} region, length of this sequence is {} \n".format(type, len(seq)))
            f.write(seq)

if exon_number == 1:
    #only 1 exon, it is at middle of the total 
    add_seq_to_file(frag1, "noncoding",1)
    add_seq_to_file(frag2, "coding")
    add_seq_to_file(frag3, "noncoding",2)
    #create a file with 2 noncoding regions
    add_seq_to_file(frag1+frag3, "noncoding")
elif exon_number == 2:
    #2 exons, it is at the start and the end of the total sequence
    add_seq_to_file(frag1, "coding",1)
    add_seq_to_file(frag2, "noncoding")
    add_seq_to_file(frag3, "coding",2)
    #create a file with 2 coding regions
    add_seq_to_file(frag1+frag3, "coding")
else:
    print("exon number excess the limit")
