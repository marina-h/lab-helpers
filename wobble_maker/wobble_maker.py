from collections import OrderedDict

# ask for primer sequence with flanking "/"s
primer = raw_input("\nWhat is your primer sequence?                      \
					\nPlease flank the codon containing the point mutation with '/' symbols, \
					\nand insert spaces between codons. \
					\nExample: AAA TTT /GGG/ CCC GGG \
					\n> ").upper()

# this code was found online
bases = ['T', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

# split primer seq into codons based on spaces and annotate with protein codes
def pretty_protein_code(split_primer):
	protein_codes = ' '
	# keep track of non-codons at edges of primer
	n_of_noncodons = 0
	for chunk in split_primer:
		if len(chunk) < 3:
			n_of_noncodons += 1
			protein_codes += '-' * len(chunk) + ' '
		elif '/' in chunk:
			protein_codes += '  ' + codon_table[chunk[1:4]] + '   '
		else:
			protein_codes += ' ' + codon_table[chunk] + '  '
	return protein_codes

print "\nYour primer sequence and its protein translation is:\n5'", primer
primer_translation = pretty_protein_code(primer.split())
print " ", primer_translation

# ask for number of changes to be made on right and left side
left_changes  = int(raw_input("\nHow many wobble changes do you want to the left? \
	                       \n> "))
right_changes = int(raw_input("\nTo the right? \
	                       \n> "))

# Summarize input about wobble changes to be made
print "\nYou want %s wobble change(s) on the right, and %s wobble change(s) on the left.\n" % (
	  left_changes, right_changes)

# make dict of codons:AA of primer excluding incomplete codons
def codons_only(p):
	return [n for n in p.split(' ') if len(n) >= 3]

## primer_dict = OrderedDict(zip(codons_only(primer), primer_translation.split()))

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

AA_list = primer_translation.split()

# mutate wobble positions (next codon with same AA in codon_table)
def wobble(primer):
	mut_codon_list = primer.split()
	pos = find_pt_mutation_pos(mut_codon_list)
	start_r = 1
	start_l = 1

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
	return mut_codon_list

print wobble(primer)
