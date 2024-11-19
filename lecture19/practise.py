#!/usr/bin/env python3
import os
import matplotlib.pyplot as plt

current_dir = "/home/s2647596/local_git_files/lecture19"
os.chdir(current_dir)

#DNA sequence file
with open("/localdisk/data/BPSM/Lecture19/ecoli.txt", mode="r") as f:
    result_seq = f.read().rstrip()[0:100000]

#window silding function
def window_slide(seq, offset, size):
    result_list = []
    for i in range(0, len(seq)-size, offset):
        result_list.append(seq[i:i+size])
    return result_list

#count the density of each nucleotide in each sequence fragment
size = 10000
frag_list = window_slide(result_seq, 1, size)
a = []
t = []
c = []
g = []
for fragment in frag_list:
    fragment = fragment.upper()
    a.append(fragment.count("A")/size)
    t.append(fragment.count("T")/size)
    c.append(fragment.count("C")/size)
    g.append(fragment.count("G")/size)

#plot the result
plt.plot(a, color="pink", label="A")
plt.plot(t, color="skyblue", label="T")
plt.plot(c, color="steelblue", label="C")
plt.plot(g, color="orange", label="G")
plt.legend()
plt.title("Base composition in the E coli genome")
plt.ylabel("Fraction of bases")
plt.xlabel("Position on genome")
plt.savefig("Chart_16A.png",transparent=True)
plt.show()
    
