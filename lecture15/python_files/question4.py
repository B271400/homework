#!/usr/bin/env python3

#K-mers are short DNA subsequences with length=k
#write a function, given any DNA sequence, print all the k-mers that occur more than n times
test_seq = "ATGCATCATG"
def count_kmer(seq, size, n,offset=1):
    count = 0 
    kmer_list= []
    while True:
        if count+size > len(seq):
            break
        result = seq[count:count+size]
        kmer_list.append(result)
        count += offset
    
    #print the kmers occur more than n times
    result_list = list(filter(lambda e: kmer_list.count(e)>n, kmer_list))
    #remove duplicated result
    return list(set(result_list))

print(count_kmer(test_seq, 2, 2))

