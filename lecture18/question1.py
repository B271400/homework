#!/usr/bin/env python3
import re

acc_list = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]
#find and print only the accessions that satisfy the following criteria individually

#create a function:
def find_acc(reg, target_list):
    reg = reg
    result_list = []
    for target in target_list:
        if re.search(reg, target):
            result_list.append(target)
    return(result_list)

#1. contain number 5
reg = r"5"
print(find_acc(reg,acc_list))

#2. contain letter d or e
reg = r"[de]"
print(find_acc(reg, acc_list))

#3. contain the letter d and e in that order (d before e)
reg = r"d.*e"
print(find_acc(reg, acc_list))

#4. contain d and e in that order with 1 letter between them
reg = r"d[a-zA-Z]{1}e"
print(find_acc(reg, acc_list))

#5. contain both the letter d and e in any order
reg1 = r"d.*e"
reg2 = r"e.*d"
result_list = []
for acc in acc_list:
    if re.findall(reg1,acc) or re.findall(reg2,acc):
        result_list.append(acc)
print(result_list)

#6. start with x or y
reg = r"^[xy]"
print(find_acc(reg, acc_list))

#7. start with x or y and end with e
reg = r"^[xy].*e$"
print(find_acc(reg, acc_list))

#8. contains any 3 numbers in any order
reg = r"\d"
result_list = []
for acc in acc_list:
    if len(re.findall(reg, acc)) == 3:
        result_list.append(acc)
print(result_list)

#9. contain 3 different numbers in th accession
reg = r"\d"
result_list = []
for acc in acc_list:
    return_list = re.findall(reg, acc)
    if len(set(return_list)) == 3 and len(return_list) == 3:
        result_list.append(acc)
print(result_list)

#10. contain 3 or more numbers
reg = r"\d"
result_list = []
for acc in acc_list:
    if len(re.findall(reg,acc)) >= 3:
        result_list.append(acc)
print(result_list)

#11. end with d followed by eighter a r or p
reg = r"d[arp]$"
print(find_acc(reg, acc_list))