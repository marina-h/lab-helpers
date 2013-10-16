Lab Helpers
=============

Some small programming projects for practicing Python!

**primer_helper.py:**

This is a simple python script that:

1. Calculates the simple melting temperature of the primer (A/T=2°C and G/C=4°C)
2. Prints the reverse complement of the primer

**primer_helper+biopython.py**

This script gives the same result as the above, but uses the biopython module for practice.
	
**wobble_maker.py:**

This is a python script that helps design specialized primers for oligo recombineering. 
The primer printed as the result can be used to create point mutations in *E. coli* strains that are not *mutS-*.

1. Takes a primer sequence with the codon with the mutation(s) flanked by "/" (e.g. AAA TTT /GGG/ CCC GGG)
2. Modifies the primer to include the specified number of wobble changes to the left and right of the mutation. 
The changes do not change the amino acid sequence of the primer.
