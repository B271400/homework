#!/usr/bin/env python3


seq  = "ATGCATCATG"
#write a programme givent any DNA sequence, will print all the k-mers that occur more than some number of times n
def sliding_window(offset, size, seq):
    count = 0
    result_list = []
    while True:
        if count+size > len(seq):
            break
        fragment = seq[count:count+size]
        result_list.append(fragment)
        count += offset
    return result_list


#given any DNA sequence, print all the k-mers(fragment with k bases) occur more than n times
def find_kmer(kmer_size, n, seq):
    result_list = sliding_window(1,kmer_size,seq)
    duplicate_list = []
    for kmer in result_list:
        if kmer in duplicate_list:
            continue
        else:
            if result_list.count(kmer) > n:
                print(f"{kmer} present {result_list.count(kmer)} times")
                duplicate_list.append(kmer)

find_kmer(2,2,seq)

