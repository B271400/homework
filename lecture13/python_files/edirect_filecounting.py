#!/usr/bin/env python3
import os, subprocess
import string

#what things are in your edirect directory?
edirect_path = "/home/s2647596/edirect"
file_names = os.listdir(edirect_path)

#how many files start with the letter e or x?
new_file_names = []
for fi in file_names:
    if fi.startswith("e") or fi.startswith("x"):
        new_file_names.append(fi)
print("there are {} files start with letter e or x".format(len(new_file_names)))

#what directory items start with the letter e or x?
for f in new_file_names:
    f_path = edirect_path+"/"+f
    #check which one is the directory
    if os.path.isdir(f_path):
        print(f)
