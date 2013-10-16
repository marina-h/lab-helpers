#!/usr/bin/env python
# -*- coding: utf8 -*-
import readline 

###tried to ask user for correct splitting of primer, but don't know how to handle "/"
# # useful function to produce list of chunks from str as str
# def chunk_str(str, chunk_size):
# 	return [str[i:i+chunk_size] for i in range(0, len(str), chunk_size)]

# this code was found online
bases = ['T', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

# split primer seq into codons based on spaces and annotate with protein codes
def pretty_protein_code(split_primer):
	protein_codes = ' '
	for chunk in split_primer:
		if len(chunk) < 3:
			protein_codes += '-' * len(chunk) + ' '
		elif '/' in chunk:
			protein_codes += '  ' + codon_table[chunk[1:4]] + '   '
		else:
			protein_codes += ' ' + codon_table[chunk] + '  '
	return protein_codes

# find postion of pt mutation
def find_pt_mutation_pos(l):
	pt_mut_pos = 0
	for x in l:
		if '/' not in x:
			pt_mut_pos += 1
		elif '/' in x:
			return pt_mut_pos
		else:
			print "Error: Primer does not specify locaiton of pt mutation with '/'"

# mutate wobble positions (next codon with same AA and same first two codons in codon_table)
def wobble(primer):
	mut_codon_list = primer.split()
	pos = find_pt_mutation_pos(mut_codon_list)
	start_r = 1
	start_l = 1

	try:
		for right in range(right_changes):
			to_mut = mut_codon_list[pos+start_r]
			for c in codon_table:
				if codon_table[c] == AA_list[pos+start_r] and c[:2]==to_mut[:2] and c != to_mut:
					mut_codon_list[pos+start_r] = c
					break
			start_r += 1

		for left in range(left_changes):
			to_mut = mut_codon_list[pos-start_l]
			for c in codon_table:
				if codon_table[c] == AA_list[pos-start_l] and c[:2]==to_mut[:2] and c != to_mut:
					mut_codon_list[pos-start_l] = c
					break
			start_l += 1

	except IndexError:
		print "\nERROR: You wanted more wobble changes than possible with this primer!"

	return mut_codon_list

# ask for number of changes to be made on right and left side and summarize
while True:
	left_changes  = int(raw_input("\nHow many wobble changes do you want to the left of the mutation?\n> "))
	right_changes = int(raw_input("\nTo the right?\n> "))

	print "\nYou want %s wobble change(s) to the right, and %s wobble change(s) to the left." % (
		  left_changes, right_changes)
	print "Is this correct? (Y/N)", 
	answer = raw_input("\n> ").upper()
	if answer == "Y" or answer == "YES":
		break

# ask for primer sequence (in specified format)
print "\n------------------------------------------------------------------------"
primer = raw_input("\nWhat is the sequence of the primer you want to make wobble changes in? \
					\nPlease flank the codon containing the point mutation with '/' symbols \
					\nand insert spaces between codons. \
					\n\nExample: 'AAA TTT /GGG/ CCC GGG' without the quotes. \
					\n\n> ").upper()

# make protein translation of primer and corresponding list of 1-letter AA abbreviations
primer_translation = pretty_protein_code(primer.split())
AA_list = primer_translation.split()

# print out new and old primers with their translations
len_primer = len(primer.replace("/","").replace(" ",""))

print "\nYour original primer sequence and its protein translation is:\n5'", primer, "(%s bp)" % len_primer
print " ", primer_translation

new_primer = " ".join(wobble(primer))
print "\nYour new primer sequence and its protein translation is:\n5'", new_primer, "(%s bp)" % len_primer
print " ", pretty_protein_code(new_primer.split()), "\n"

print "Here is a copy-and-pasteable version:\n", new_primer.replace("/","").replace(" ",""), "\n"

