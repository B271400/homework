#!/usr/bin/env python3
import os, subprocess
current_path = "/home/s2647596/local_git_files/lecture13"
os.chdir(current_path)

#generate overlapping short segments from a string
#e.g. abcdefg => if choose size 3, offset 1 => 
# output: abc, bcd, cde, efg
def overlap_seg(input_str, size, offset):
    count = 0
    result_list = []
    while True:
        if count+size > len(input_str):
            break
        result = input_str[count:count+size]
        result_list.append(result)
        count += offset
    return result_list

#find the percentage GC content of each segment and the sequence
def GC_percent(seq):
    C_num = seq.count("C")
    G_num = seq.count("G")
    return (C_num + G_num)/len(seq)*100

#use the protein-coding region from AJ223353 NCBI sequence
#the remote_exon01.fasta
#generates segmetns that are 30 bases long, with a window offset of 3
with open("./resources/remote_exon01.fasta", mode="r") as f:
    result_list = f.readlines()
    seq = result_list[1]

segment_list = overlap_seg(seq, 30,3)

#print the GC percentage of the sequence
print("the GC percentage of the whole sequence is {:.2f}%".format(GC_percent(seq))) 


#print each segment to the screen
for i in range(len(segment_list)):
    seg = segment_list[i]
    print(seg)
    #print GC percentage of each segment and the sequence
    GC_percentage = GC_percent(seg)
    print("the GC percentage of this segment is {:.2f}%".format(GC_percentage))
    
    #save the segments to different fasta file
    file_name = "individual_segment{}.fasta".format(i+1)
    header_line = ">segment {}, GC percentage is {:.2f}%".format(i+1, GC_percentage)
    with open(f"./result_files/question3/{file_name}", mode="w") as f:
        f.write(header_line+"\n")
        f.write(seg)

    #save all the segments to 1 fasta file
    with open(f"./result_files/question3/total_segments.fasta", mode="a") as f:
        f.write(header_line+"\n")
        f.write(seg+"\n")
        f.write("\n")


#modify overlapping segment function, include the partial sliding window segmetns at the end
def overlap_seg_modify(input_str, size, offset):
    count = 0
    result_list = []
    while True:
        if count+size > len(input_str):
            break
        result = input_str[count:count+size]
        result_list.append(result)
        count += offset
    #different treatment to the last segment
    last_seg = result_list[-1]
    seq_count = 1
    while True:
        if seq_count >= len(last_seg) :
            break
        result = last_seg[seq_count:len(last_seg)]
        result_list.append(result)
        seq_count += offset
    return result_list

#include the partial sliding window segments 
modify_seg_list = overlap_seg_modify(seq, 30, 3)
print("the segments include the partial sliding window segments")
for seg in modify_seg_list:
    print(seg)
