#!/usr/bin/env python3

#question4
seq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
#extract the first and second exon
first_exon = seq[:63]
second_exon = seq[90:]
#join 2 exons to make the coding sequence
coding_seq = first_exon+second_exon
print("coding sequence: {}".format(coding_seq))

#calculate percentage of the DNA sequence is coding
#length of coding sequence
len_coding = len(coding_seq)
percentage_coding = len_coding/len(seq)*100
print("percentage of the DNA sequence is coding is {:.2f}%".format(percentage_coding))

#coding part with uppercase
#non coding part with lowercase
converted_seq = first_exon.upper() + seq[63:90].lower()+second_exon.upper()
print("the converted sequence with uppercase coding part and lowercase noncoding part: ", converted_seq)

