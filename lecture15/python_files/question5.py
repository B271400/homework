#!/usr/bin/env python3

#the use should be asked to supply, on the command line
#the sequence, the kmer length for analysis
#the threshold frequency of kmers found
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

seq = input("what is the sequence of interest")
def test_input(input_content):
    while True:
        try:
            output_result = int(input(input_content))
        except:
            print("please enter an integer")
        else:
            return output_result
        
kmer_length = test_input("what is the kmer length?")
threshold = test_input("what is the threshold frequency of kmers found?")
kmer_list = count_kmer(seq, kmer_length,threshold)
print(f"the kmers of {seq} present more than {threshold} times are {kmer_list}")
    