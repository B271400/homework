#!/usr/bin/env python3

test_seq = ['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT'] 
#calculate for each pair of sequences, the percentage of identical positions
def calc_pair(test_seq):
    for i in range(len(test_seq)):
        for j in range(i+1,len(test_seq)):
            #seq1 is from index 0 to 3, seq 2 is from 1 to 3, 2 to 3, 3, so we could pair each seq
            seq1 = test_seq[i]
            seq2 = test_seq[j]
            count = 0
            #for loop for the base in sequences, percentage is calculate outside this loop
            for k in range (len(seq1)):
                base1 = seq1[k]
                base2 = seq2[k]
                if base1 == base2:
                    count +=1
            percent = count/len(seq1)*100
            print("the percentage of identical positions for seq {} and seq {} is {:.2f}%".format(seq1, seq2, percent))

calc_pair(test_seq)