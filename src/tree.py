from copy import copy


class Node:
	def __init__(self, 
		         operation: str = None, 
		         leftson = None, 
		         rightson = None, 
		         var: str = None
		         ):
		self.operation = operation
		self.leftson = leftson
		self.rightson = rightson
		self.var = var

	def convert_tree_to_nnf_tree(self):
		if (self.var != None):
			return copy(self)
		if (self.operation == '~'):
			next_op = self.leftson.operation
			if (next_op == None):
				return copy(self)
			if (next_op == '~'):
				return copy(self.leftson.leftson).convert_tree_to_nnf_tree()
			left = Node(operation='~', leftson=self.leftson.leftson).convert_tree_to_nnf_tree()
			right = Node(operation='~', leftson=self.leftson.rightson).convert_tree_to_nnf_tree()
			if (next_op == '&'):
				return Node(operation='|', leftson=left, rightson=right)
			if (next_op == '|'):
				return Node(operation='&', leftson=left, rightson=right)
		return Node(operation=self.operation, 
			        leftson=self.leftson.convert_tree_to_nnf_tree(),
			        rightson=self.rightson.convert_tree_to_nnf_tree()
			        )

	def convert_tree_to_normal_form(self, normal_form_name: str) -> [[str]]:
		if (self.var != None):
			return [[self.var]]
		if (self.operation == '~'):
			return [['~' + self.leftson.var]]
		inside_op, outside_op = '&', '|'
		if normal_form_name == 'CNF':
			inside_op, outside_op = outside_op, inside_op
		left_clauses = self.leftson.convert_tree_to_normal_form(normal_form_name)
		right_clauses = self.rightson.convert_tree_to_normal_form(normal_form_name)
		if (self.operation == inside_op):
			clauses: [[str]] = []
			for left_clause in left_clauses:
				for right_clause in right_clauses:
					clauses.append([*left_clause, *right_clause])
			return clauses
		if (self.operation == outside_op):
			left_clauses.extend(right_clauses)
			return left_clauses
			