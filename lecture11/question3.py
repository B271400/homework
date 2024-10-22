#!/usr/bin/env python3

#question3
seq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
motif = "GAATTC"

#find the start point of the motif
start_point = seq.find(motif)
print("start position of the moditf in the sequence is at: {}".format(start_point))

#find cut position, it is between first and second nucleotide of the motif
cut_point = start_point+1
#the length of first sequence fragment
length_1 = cut_point
#length of second sequence fragment
length_2 = len(seq)-length_1

print("length of first sequence is {}, second sequence is {}, total seq length is {}".format(
    length_1, length_2, len(seq)
))
