#!/usr/bin/env python3

seq="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

#print the complement of this sequence
com_seq = seq.replace("A","t").replace("T","a").replace("G","c").replace("C","g").upper()
print("the complement sequence is: ",com_seq)
