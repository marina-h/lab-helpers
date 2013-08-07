#!/usr/bin/env python
# -*- coding: utf8 -*-
import Bio
from Bio.Seq import Seq
'''
1. Asks for primer sequence
2. Returns Tm (simple calculation) and reverse complement
'''

primer = raw_input("\nWhat is your primer sequence?\n> ").upper()
primer_seq = Seq(primer)

def melting_temp(p):
	Tm = 0
	for n in p:
		if n == 'A' or n == 'T':
			Tm += 2
		if n == 'G' or n == 'C':
			Tm += 4
	return Tm 

print "\nYour primer sequence is:\n5' ", primer_seq
print "\nIts reverse complement is:\n5' ", primer_seq.reverse_complement()
print "\nThe Tm of this primer (A,T=2°C, G,C=4°C) is:\n", melting_temp(primer), "°C\n"