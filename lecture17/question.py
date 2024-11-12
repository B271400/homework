#!/usr/bin/env python3
import os
import pandas as pd
import numpy as np
import re

#set the working directory
working_dir = "/home/s2647596/local_git_files/lecture17"
os.chdir(working_dir)

#obtain the data file
eu_table = pd.read_csv("./resources/data.csv", sep="\t", na_values=['-'])
#show all the column names
# print(eu_table.columns)

#question1: 
# how many fungal species have genomes > 100Mb
result_num = eu_table[(eu_table["Size (Mb)"] > 100) & (eu_table["Group"] == "Fungi")]["Group"]
print(f"there are {len(result_num)} fungal species have genomes > 100Mb")
#what are their names?
species_name = eu_table[(eu_table["Group"]=="Fungi") & (eu_table["Size (Mb)"] > 100)]["#Organism/Name"].value_counts()
species_list = list(species_name.index)
print(f"here is the name of these fungal species: {species_list}")

#question2
#how many of each group have been sequenced
print("sequence for each group")
seq_num = eu_table["Group"].value_counts()
print(seq_num)
#count the unique
print("unique sequence for each group")
new_table = eu_table.drop_duplicates("#Organism/Name")
print(new_table["Group"].value_counts())

#question 3
#which Heliconius species genomes have been sequenced
Heliconius_table= eu_table[eu_table.apply(lambda row: row["#Organism/Name"].startswith("Heliconius"), axis=1)][["#Organism/Name","Scaffolds", "Assembly Accession"]]
Heliconius_list = list(Heliconius_table.drop_duplicates("#Organism/Name")["#Organism/Name"])
#print(Heliconius_list)
#how many scaffolds is each assembly in?
print(Heliconius_table[["#Organism/Name","Scaffolds"]])


#question4
#which sequencing centre has sequenced the most plant genomes?
center_series = eu_table[eu_table["Group"]=="Plants"]["Center"].value_counts()
center_name = center_series.index[0]
print(f"the center {center_name} has sequenced the most plant genomes")
#which sequencing center has sequenced the most insect genomes?
center_series = eu_table[eu_table["SubGroup"] == "Insects"]["Center"].value_counts()
center_name = center_series.index[0]
print(f"the center {center_name} sequneced the most insect genomes")

#question5
#add a column giving the number of proteins per gene
new_column = eu_table.apply(lambda row: row["Proteins"]/row["Genes"], axis=1)
eu_table["Protein_concentration"] = new_column
#treat NA as -1, which is different from the correct data, and avoid str value error
eu_table["Protein_concentration"] = eu_table["Protein_concentration"].fillna(-1)
# print(eu_table["Protein_concentration"])

#which genomes have at least 10% more protein than genes
more_p_table = eu_table[eu_table["Protein_concentration"] >= 1.1][["#Organism/Name","Protein_concentration"]]
print(more_p_table)
#number of genomes have >= 1.1 
num_p = len(more_p_table)
print(f"there are {num_p} number of genomes have >= 1.1")