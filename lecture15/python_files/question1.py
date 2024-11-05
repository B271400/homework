#!/usr/bin/env python3

#function takes 2 arguments (protein seq and a amino acid residue code)
#return percentage of the protein that the amino acid makes up
def AA_percent(protein_seq, AA_code):
    percentage = (protein_seq.count(AA_code))/len(protein_seq) *100
    return int(percentage)

def assert_test(func,expected_value,*args):
    result = func(*args)
    try:
        assert result == expected_value, f"expected result is {expected_value},but outcome is {result}"
    except AssertionError as e:
        print(e)
    else:
        print(f"expected result and real outcome are same: {result}")

#test the function
assert_test(AA_percent, 5, "MSRSLLLRFLLFLLLLPPLP", "M")
assert_test(AA_percent,10,"MSRSLLLRFLLFLLLLPPLP", "r")
assert_test(AA_percent,50,"MSRSLLLRFLLFLLLLPPLP", "L")
assert_test(AA_percent,0,"MSRSLLLRFLLFLLLLPPLP", "Y")