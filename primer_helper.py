#!/usr/bin/env python
# -*- coding: utf8 -*-
import readline 

reverse_comp_dict = {'A':'T', 'T':'A','G':'C', 'C':'G'}

def melting_temp(p):
	Tm = 0
	for n in p:
		if n == 'A' or n == 'T':
			Tm += 2
		if n == 'G' or n == 'C':
			Tm += 4
	return Tm 

def reverse_comp(p):
	reverse = ""
	for n in p[::-1]:
		reverse += reverse_comp_dict[n]
	return reverse

while True:
	print "--------------------START--------------------"

	primer = raw_input("\nWhat is your primer sequence? \
		\n(Press CTRL-C to terminate program.)          \
		\n> ").upper()

	print "\nYour primer sequence is:\n5' %s (%s bp)\n" % (primer, len(primer))
	print "Its reverse complement is:\n5'", reverse_comp(primer), "(%s bp)\n" % len(primer)
	print "The Tm of this primer (A,T=2°C, G,C=4°C) is:\n", melting_temp(primer), "°C"
	print "\n"