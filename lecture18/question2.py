#!/usr/bin/env python3
import os
import re

#obtain the DNA sequence from the file
current_dir = "/home/s2647596/local_git_files/lecture18"
os.chdir(current_dir)

with open("./seq.txt", mode="r") as f:
    seq = f.read().rstrip()

#1. what fragment lengths will we get if we digest the sequence with a restriction enzyme 
#with recognition site ANT*AAT, * is the cut site
reg = r"A[ATCG]TAAT"
matches = re.finditer(reg, seq)
cut_list = []
for match in matches:
    cut_point = match.start()+3
    cut_list.append(cut_point)
frag_length = []
for i in range(len(cut_list)):
    if i==0:
        frag_length.append(cut_list[i])
    else:
        frag_length.append(cut_list[i]-cut_list[i-1])
        if i==len(cut_list)-1:
            frag_length.append(len(seq)-cut_list[i])
print(f"the fragment length list: {frag_length}")

# what are the sequence of the fragment
frag_list = []
for i in range(len(frag_length)):
    if i==0:
        frag_list.append(seq[0:frag_length[i]])
        current_position = frag_length[i]
    else:
        frag_list.append(seq[current_position:current_position+frag_length[i]])
        current_position += frag_length[i]
# print(frag_list)

#2. what will the fragment length be if we do a double digest with both ANT*AAT and GCRW*TG
reg = r"(?:A[ATCG]TAAT)|(?:GC[AG][AT]TG)"
#find all the enzyme cutting position
enzyme_list = re.findall(reg,seq)
cut_point_list = []
for enzyme in enzyme_list:
    match = re.search(enzyme, seq)
    match_text = match.group()
    #different cut point for two enzyme
    if re.search("^A",match_text):
        cut_point = match.start()+3
    else:
        cut_point = match.start()+4
    cut_point_list.append(cut_point)

print(cut_point_list)
frag_length = []
frag_list = []
#the length of each fragment
for i in range(len(cut_point_list)):
    if i==0:
        end_point = cut_point_list[i]
        frag_list.append(seq[0:end_point])
        frag_length.append(end_point)
    else:
        start_point = cut_point_list[i-1]
        end_point = cut_point_list[i]
        frag_list.append(seq[start_point:end_point])
        frag_length.append(end_point - start_point)
        if i == len(cut_point_list)-1:
            frag_list.append(seq[end_point:len(seq)])
            frag_length.append(len(seq)-end_point)

print(f"the fragment length list: {frag_length}")
#print(frag_list)