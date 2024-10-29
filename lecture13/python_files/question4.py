#!/usr/bin/env python3
import os, subprocess
current_path = "/home/s2647596/local_git_files/lecture13"
os.chdir(current_path)

#creates 9 new 'size range' directories
# one for sequences between 100-199 long
#one for sequence between 200-299 long etc..

#get the DNA sequence files name
all_names = os.listdir("./resources")
#filter the file name end with .dna
file_names = []
for name in all_names:
    if name.endswith(".dna"):
        file_names.append(name)

#create 9 directories
dir_names = []
for i in range(9):
    dir_name = f"size_{i+1}00_{i+1}99"
    dir_names.append(dir_name)
    os.mkdir(f"./result_files/question4/{dir_name}")

#find the length of each sequence, save in a new file, allocate them to correct directory
for f_name in file_names:
    f_pure_name = f_name.split(".")[0]
    with open("./resources/{}".format(f_name)) as f:
        lines = f.readlines()
        for sequence in lines:
            seq_length = len(sequence)
            length_type = str(seq_length)[0]
            # print(seq_length, length_type)
            #create a new file
            new_file_name = f"{f_pure_name}_{seq_length}.dna"
            #different treatment to sequence length more then 1000
            if seq_length < 1000:
                current_dir = f"size_{length_type}00_{length_type}99"
            else:
                current_dir = f"size_900_999"
            #allocate the file to correct directory
            with open("./result_files/question4/{}/{}".format(current_dir,new_file_name), mode="w") as inner_f:
                inner_f.write(sequence.upper())



                

