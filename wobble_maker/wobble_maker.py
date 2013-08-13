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
	for chunk in split_primer:
		if len(chunk) < 3:
			protein_codes += '' * len(chunk) + '  '
		elif '/' in chunk:
			protein_codes += '  ' + codon_table[chunk[1:4]] + '   '
		else:
			protein_codes += ' ' + codon_table[chunk] + '  '
	return protein_codes

print "\nYour primer sequence and its protein translation is:\n5'", primer
print " ", pretty_protein_code(primer.split())


# ask for position of point mutation in codon (1, 2, or 3)
codon_pos = [1,2,3]
while True:
	mut_pos_in_codon = int(raw_input(
					"\nWhat is the position of the mutation in the codon? \
					\nType in 1, 2, or 3.                                 \
					\n> "))
	if mut_pos_in_codon not in codon_pos:
		print "Error: Position in codon must be one of 1, 2, or 3!"
		print "----------------------------------------------------"
	else:
		break

# ask for number of changes to be made on right and left side
left_changes  = raw_input("\nHow many wobble changes do you want to the left? \
	                       \n> ") 
right_changes = raw_input("\nTo the right? \
	                       \n> ")

# Summarize input
print "\nYou want %s wobble changes on the right, and %s wobble changes on the left.\n" % (
	  left_changes, right_changes)

# mutate wobble positions


# useful function to produce list of chunks as strings
# def chunk_str(str, chunk_size):
#    return [str[i:i+chunk_size] for i in range(0, len(str), chunk_size)]
