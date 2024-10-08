#!/bin/bash

#combine all the sequence files into one file
while read name
do
	echo "processing file: ${name}.fasta";
	#read each fasta file and paste the contents in them to a new file
	while read content
	do
		echo -e "${content}\n" >> total.fasta
	done < ./sequence_files/${name}.fasta;
done < acc.txt

