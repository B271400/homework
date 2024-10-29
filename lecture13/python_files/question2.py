#!/usr/bin/env python3
import os, subprocess

current_path = "/home/s2647596/local_git_files/lecture13"
os.chdir(current_path)

#file genomic_dna2.txt contains a section of genomic DNA
#file exons.txt contains a list of start/ stop positions of exons
#extract the exon segments, concatenate them, write them to a new file

#obtain the start and end position of each exon from exons.txt file
with open("./resources/exons.txt", mode="r") as f:
    position_list = []
    lines = f.readlines()
    for position in lines:
        #remvoe the \n symbol
        position = position[:-1]
        #seperate the start point and end point, add them into a list
        temp_list = position.split(",")
        position_list.append(temp_list)
    # print(position_list)

#obtain the exons using start-end position list
with open("./resources/genomic_dna2.txt", mode="r") as f:
    dna_result = f.read().rstrip("\n")
    # print(dna_result)
    #save exons in a list
    exon_list = []
    for position in position_list:
        start = int(position[0])
        end = int(position[1])
        exon = dna_result[start-1:end]
        exon_list.append(exon)


#combine all the exons, save them in a new file
with open("./result_files/question2.txt", mode="w") as f:
    result_str = "".join(exon_list)
    f.write(result_str)
