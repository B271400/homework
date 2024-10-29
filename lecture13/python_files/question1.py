#!/usr/bin/env python3

#processing DNA in a file
#1 sequence per line, each sequence starts with the same 14 base pairs
#remove the first 14 base pair, save in a new file
#print the length of each new sequence to the screen
file_path = "/home/s2647596/local_git_files/lecture13/resources"
with open("{}/input.txt".format(file_path), mode="r") as f:
    trim_seq_list = []
    f_lines = f.readlines()
    for seq in f_lines:
        #remove the initial 14 base pairs
        new_seq = seq[14:]
        #save the new sequence into a list,remove the \n at the end
        trim_seq_list.append(new_seq[:-1])

#save the result in a new file
result_path = "/home/s2647596/local_git_files/lecture13/result_files"
with open(f"{result_path}/question1.txt",mode="w") as f:
    for i in range(len(trim_seq_list)):
        f.write(trim_seq_list[i]+"\n")
        #print the length of each new sequence
        print(f"the length of new sequence {i+1} is: {len(trim_seq_list[i])}")

