#!/usr/bin/env python3
import os
import matplotlib.pyplot as plt
import numpy as np

current_dir = "/home/s2647596/local_git_files/lecture19"
os.chdir(current_dir)

#DNA sequence file
with open("/localdisk/data/BPSM/Lecture19/ecoli.txt", mode="r") as f:
    genome_50000 = f.read().rstrip()[0:50000]
    genome_100000 = f.read().rstrip()[0:100000]
    whole_genome = f.read().rstrip()

def show_AT(seq, offset, size, question_num):
    #window sliding
    frag_list = []
    for i in range(0, len(seq)-size, offset):
        frag_list.append(seq[i:i+size])

    #count the density of AT density in each sequence fragment
    at = []
    for fragment in frag_list:
        fragment = fragment.upper()
        at.append((fragment.count("A")+fragment.count("T"))/size)

    #plot the result
    plt.plot(at, color="skyblue")
    plt.title("AT composition in the E coli genome")
    plt.ylabel("Fraction of bases")
    plt.xlabel("Position on genome")
    plt.savefig(f"question_{question_num}.png",transparent=True)
    plt.show(block=False)


show_AT(genome_50000, 1, 1000,1)
show_AT(genome_100000, 1, 1000,2)
show_AT(whole_genome, 1, 1000,3)
