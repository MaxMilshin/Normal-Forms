import unittest

import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from parser import Parser 
from converter import Converter

class Test(unittest.TestCase):
	def test_parse_unparse(self):
		parser = Parser()
		formulas = [
			'(xx & y) | (~x & ~y)',
			'(x & y) | (~x & y) | (~x & ~y) | (x & ~y)',
			'~(x & y) | ~(x | y)'
		]
		answers = [
			'xx & y | ~x & ~y',
			'x & y | ~x & y | ~x & ~y | x & ~y',
			'~(x & y) | ~(x | y)'
		]
		for formula, answer in zip(formulas, answers):
			tree = parser.parse(formula)
			out_formula = parser.unparse(tree)
			self.assertEqual(out_formula, answer) 

	def test_convert_to_NNF(self):
		parser = Parser()
		formulas = [
			'~(xx & y)',
			'~((x & y) | (~x & y))',
			'~~~~(~x)'
		]
		answers = [
			'~xx | ~y',
			'(~x | ~y) & (x | ~y)',
			'~x'
		]
		for formula, answer in zip(formulas, answers):
			tree = parser.parse(formula)
			nnf_tree = tree.convert_to_NNF()
			out_formula = parser.unparse(nnf_tree)
			self.assertEqual(out_formula, answer) 

	def test_convert_to_NNF(self):
		converter = Converter()
		formulas = [
			'~(xx & y)',
			'~((x & y) | (~x & y))',
			'~~~~(~x)'
		]
		answers = [
			'~xx | ~y',
			'(~x | ~y) & (x | ~y)',
			'~x'
		]
		for formula, answer in zip(formulas, answers):
			self.assertEqual(converter.convert_to_NNF(formula), answer)

	def test_convert_to_DNF(self):
		converter = Converter()
		formulas = [
			'(x | y) & (a | b)'
		]
		answers = [
			'(x & a) | (x & b) | (y & a) | (y & b)'
		]
		for formula, answer in zip(formulas, answers):
			self.assertEqual(converter.convert_to_DNF(formula), answer)


	def test_convert_to_CNF(self):
		converter = Converter()
		formulas = [
			'(x | y) & (a | b)',
			# '(x & y) | (x1 & y1)'
		]
		answers = [
			'(x | y) & (a | b)',
			'(x | x1) & (x | y1) & (y | x1) & (y | y1)'
		]
		for formula, answer in zip(formulas, answers):
			self.assertEqual(converter.convert_to_CNF(formula), answer)
		