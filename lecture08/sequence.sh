#!/bin/bash

#obtain the fasta sequence result from the accession number file
while read acc
do
	echo -e "Downloading ${acc}";
	wget -O ${acc}.fasta "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=${acc}&strand=1&rettype=fasta&retmode=text";
done < acc.txt
