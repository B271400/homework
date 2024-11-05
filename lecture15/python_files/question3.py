#!/usr/bin/env python3

def base_counter(seq, threshold):
    normal_bases = ['A','T','C','G']
    seq = seq.upper()
    #the number of each base in the sequence
    base_count = list(map(lambda e: seq.count(e), normal_bases))
    #the percentage of not base in the sequence
    not_base_percent = (1-sum(base_count)/len(seq))*100
    if not_base_percent>threshold:
        return 0
    else:
        return 1

def assert_test(func, *args):
    try:
        assert func(*args), f"the percent of not bases in the sequence exceed threshold"
    except AssertionError as a:
        print(a)
    else:
        print("the percent of not bases in the sequence is acceptable")
        
assert_test(base_counter, "MSRSLLLRFLLFLLLLPPLPAAGTTTT", 30)
assert_test(base_counter, "MSRSLLLRFLLFLLLLPPLPAAGTTTT", 90)