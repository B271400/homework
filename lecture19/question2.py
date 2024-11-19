#!/usr/bin/env python3

import os
import matplotlib.pyplot as plt

current_dir = "/home/s2647596/local_git_files/lecture19"
os.chdir(current_dir)

def genome_analyse(content_type, portion, species_name="ecoli"):
    portion = int(portion)
    #DNA sequence file
    with open(f"/localdisk/data/BPSM/Lecture19/{species_name}.txt", mode="r") as f:
        result_seq = f.read().rstrip()[0:portion]

    #window sliding
    size = 1000
    frag_list = []
    for i in range(0, len(result_seq)-size):
        frag_list.append(result_seq[i:i+size])

    #count the density of AT density in each sequence fragment
    content_density_list = []
    for fragment in frag_list:
        fragment = fragment.upper()
        if content_type.upper() == "AT" or content_type.upper() == "TA":
            content_density_list.append((fragment.count("A")+fragment.count("T"))/size)
        elif content_type.upper() == "GC" or content_type.upper() == "CG":
            content_density_list.append((fragment.count("C")+fragment.count("G"))/size)

    #plot the result
    plt.plot(content_density_list, color="skyblue")
    plt.title(f"{content_type} composition in the {species_name} genome")
    plt.ylabel("Fraction of bases")
    plt.xlabel("Position on genome")
    plt.savefig(f"{species_name}_{portion}.png",transparent=True)
    plt.show()

#usr provide the window size, AT or GC content, what portion of the genome they want analysed
species_name = input("what is the species name of the genome?")
content_type = input("AT or GC")
portion = input("what portion of genome want to analyse?")
genome_analyse(content_type, portion, species_name)
