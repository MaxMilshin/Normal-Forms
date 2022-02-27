from parser import Parser
from tree import Node

class Converter:
	def convert_to_NNF(self, formula: str) -> str:
		parser = Parser()
		tree = parser.parse(formula)
		nnf_tree = tree.convert_tree_to_nnf_tree()
		nnf_formula = parser.unparse(nnf_tree)
		return nnf_formula

	def convert_to_DNF(self, formula: str) -> str:
		parser = Parser()
		tree = parser.parse(formula)
		nnf_tree = tree.convert_tree_to_nnf_tree()
		clauses = nnf_tree.convert_tree_to_normal_form(normal_form_name='DNF')
		dnf_formula = parser.unparse_to_normal_form(clauses, normal_form_name='DNF')
		return dnf_formula

	def convert_to_CNF(self, formula: str) -> str:
		parser = Parser()
		tree = parser.parse(formula)
		nnf_tree = tree.convert_tree_to_nnf_tree()
		clauses = nnf_tree.convert_tree_to_normal_form(normal_form_name='CNF')
		cnf_formula = parser.unparse_to_normal_form(clauses, normal_form_name='CNF')
		return cnf_formula