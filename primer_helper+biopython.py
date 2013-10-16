#!/usr/bin/env python
# -*- coding: utf8 -*-
import Bio
from Bio.Seq import Seq
import readline 

while True:
	print "--------------------START--------------------"
	primer = raw_input("\nWhat is your primer sequence? \
		\n(Press CTRL-C to terminate program.)          \
		\n> ").upper()
	primer_seq = Seq(primer)

	def melting_temp(p):
		Tm = 0
		for n in p:
			if n == 'A' or n == 'T':
				Tm += 2
			if n == 'G' or n == 'C':
				Tm += 4
		return Tm 

	print "\nYour primer sequence is:\n5'", primer_seq, "(%s bp)" % len(primer)
	print "\nIts reverse complement is:\n5'", primer_seq.reverse_complement(), "(%s bp)" % len(primer)
	print "\nThe Tm of this primer (A,T=2°C, G,C=4°C) is:\n", melting_temp(primer), "°C\n"