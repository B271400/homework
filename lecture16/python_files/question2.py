#!/usr/bin/env python3

#a dict that stores a codon usage table for translation
gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

#take any DNA sequence and translate it into protein using the translation table
test_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
def convert_seq(seq):
    seq = seq.upper()
    seq_list = []
    i=0
    while True:
        if i+3 > len(seq):
            if i+3 != len(seq):
                seq_list.append(seq[i:len(seq)])
            break
        seq_list.append(seq[i:i+3])
        i += 3
    
    #remove a potential blank value at the end of the list
    if len(seq_list[-1]) == 0:
        seq_list.pop(-1)

    protein_list = []
    for codon in seq_list:
        if codon in gencode.keys():
            protein_list.append(gencode[codon])
        else:
            protein_list.append("_")
    return "".join(protein_list), seq_list

result, seq_list = convert_seq(test_seq)
print(result)

#generate a translation in all 3 forward frames
def translate_forward(seq):
    protein, seq_list = convert_seq(seq)
    num = len(seq_list[-1])%3
    if num == 0:
        type=0
    if num == 1:
        type=2
    if num == 2:
        type=1
    seq1 = " ".join(seq_list)
    print(f"{seq1} -->  {type+1}")
    print(f"translation result: {protein}")

#3 frames
def three_forward(seq):
    for i in range(0, 3):
        translate_forward(seq[i:])

three_forward(test_seq)
three_forward("ATGXMCGTGACGAGGGT")

#generate a translation in all 3 reverse frames
def translate_reverse(seq):
    seq = seq.upper()
    reverse_seq = seq.replace("A",'t').replace("T",'a').replace("C",'g').replace("G",'c')
    reverse_seq = reverse_seq.upper()
    num = len(reverse_seq)%3
    if num == 0:
        protein, seq_list = convert_seq(reverse_seq)
        type = 0
    else:
        new_seq = reverse_seq[num:]
        protein, seq_list = convert_seq(new_seq)
        seq_list.insert(0,reverse_seq[0:num])
        if num == 1:
            type=2
        if num == 2:
            type=1
    

    print(f"original sequence: {seq}")
    print(f"{type+1} <-- {' '.join(seq_list)}")
    print(f"translation result: {protein}")

#3 frames
def three_reverse(seq):
    for i in range(0, 3):
        translate_reverse(seq[i:])

three_reverse(test_seq)
three_reverse("ATGTTCGTGACGAGGGT")