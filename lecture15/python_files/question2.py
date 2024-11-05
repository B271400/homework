#!/usr/bin/env python3

#count a list of amino acid residues within the protein sequence
def AA_percent(protein_seq, aa_list=["A", "I", "L", "M", "F", "W", "Y", "V"]):
    count_list = list(map(lambda e: protein_seq.count(e), aa_list))
    return int(sum(count_list)/len(protein_seq)*100)

try:
    assert AA_percent("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
    assert AA_percent("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
    assert AA_percent("MSRSLLLRFLLFLLLLPPLP") == 65
except AssertionError as e:
    print("did not pass the assert test")
else:
    print(AA_percent("MSRSLLLRFLLFLLLLPPLP", ["M"]))
    print(AA_percent("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']))
    print(AA_percent("MSRSLLLRFLLFLLLLPPLP"))