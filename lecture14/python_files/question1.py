#!/usr/bin/env python3
import os

#set up the current directory
current_dir = "/home/s2647596/local_git_files/lecture14"
os.chdir(current_dir)

#data file contain 4 fields: species name, sequences, gene name, expression level
#seperated by comma (,)

#read each line, obtain each data
with open("./resources/data.csv", mode="r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip("\n")
        row_data = line.split(",")
        species_name = row_data[0].strip()
        sequences = row_data[1].strip()
        gene_name = row_data[2].strip()
        expression_level = float(row_data[3])
        #1.print the gene names for all genes from species Drosophila melanogaster or simulans
        if (
            species_name == "Drosophila melanogaster" or species_name == "Drosophila simulans"
        ):
            print(f"question 1: {gene_name}, {species_name}")
        #2.print the gene names for gene between 90-100 bases long
        if(
            len(sequences) >= 90 and len(sequences)<=110
        ):
            print(f"question 2: {gene_name}, {len(sequences)}")
        #3.print the gene names whose AT content is less than 0.5 and whose expression level >200
        #caculate AT percentage first
        A_num = sequences.upper().count("A")
        T_num = sequences.upper().count("T")
        AT_percent = round((A_num+T_num)/len(sequences), 2)
        if(
            AT_percent < 0.5 and expression_level > 200
        ):
            print(f"question 3: {gene_name}, {AT_percent}, {expression_level}")
        #4.print the gene name whose name begins with k or h except Drosophila melanogaster
        if (
            (gene_name.startswith("k") or gene_name.startswith("h"))
            and species_name != "Drosophila melanogaster"
        ):
            print(f"question 4: {gene_name}, {species_name}")
        #5. print a message giving the gene name, saying whether its AT content is high or low or medium
        if AT_percent > 0.65:
            AT_type = "high"
        elif AT_percent < 0.45:
            AT_type = "low"
        else:
            AT_type = "medium"
        print (f"question5:{gene_name} AT content is {AT_percent}, which is {AT_type}")

        


        