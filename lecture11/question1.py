#!/usr/bin/env python3

#DNA sequence
seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"


#count the number of A in this seq
num_A = seq.count("A")
print("there are {} number of A nucleotides".format(num_A))

#count the number of T 
num_T = seq.count("T")
print("there are {} number of T nucleotides".format(num_T))

#add the number of T and A up, and divide by the length of the sequence
print("result:{:.2f}".format((num_A+num_T)/len(seq)))
