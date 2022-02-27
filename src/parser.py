from tree import Node
from stuff import is_var, is_var_char, get_priority

class Parser:
	def parse(self, s: str):
		symbols = self.__prepare(s.replace(' ', ''))
		return self.__parse(symbols)

	def unparse(self, node: Node) -> str:
		if (node.var != None):
			return node.var
		if (node.operation == '~'):
			brackets = self.__put_brackets(node.leftson, node.operation)
			state = self.unparse(node.leftson)
			if brackets:
				state = '(' + state + ')'
			return node.operation + state
		left_brackets = self.__put_brackets(node.leftson, node.operation)
		left_state = self.unparse(node.leftson)
		right_brackets = self.__put_brackets(node.rightson, node.operation)
		right_state = self.unparse(node.rightson)
		if left_brackets:
			left_state = '(' + left_state + ')'
		if right_brackets:
			right_state = '(' + right_state + ')'
		return left_state + ' ' + node.operation + ' ' + right_state		

	def unparse_to_normal_form(self, clauses: [[str]], normal_form_name: str) -> str:
		inside_op, outside_op = '&', '|'
		if normal_form_name == 'CNF':
			inside_op, outside_op = outside_op, inside_op
		formula = ""
		for j, clause in enumerate(clauses):
			clause_str = ""
			for i, literal in enumerate(clause):
				clause_str += literal
				if i != len(clause) - 1:
					clause_str += ' ' + inside_op + ' '
			if len(clause) > 1 and len(clauses) > 1: 
				clause_str = '(' + clause_str + ')'
			formula += clause_str
			if j != len(clauses) - 1:
				formula += ' ' + outside_op + ' '
		return formula


	def __prepare(self, s: str) -> [str]:
		start = 0
		symbols = []
		for i in range(1, len(s)):
			if is_var_char(s[i]) and is_var_char(s[i - 1]):
				continue
			else:
				symbols.append(s[start:i])
				start = i
		symbols.append(s[start:len(s)])
		return symbols

	
	def __parts_parse(self, operations: [str], parts: [[str]]) -> Node:
		if len(operations) == 0:
			return self.__parse(parts[0])
		for priorety in ['~', '&', '|']:
			for i, op in enumerate(operations):
				if (op == priorety):
					return Node(operation=priorety, 
						        leftson=self.__parts_parse(operations[0:i], parts[0:i+1]),
						        rightson=self.__parts_parse(operations[i+1:], parts[i+1:])
						        )

	
	def __parse(self, symbols: [str]) -> Node:
		if len(symbols) == 1:
			return Node(var=symbols[0])
		operations: [str] = []
		parts: [[str]] = []
		is_started = False
		bal = 0
		start = 0
		for i, symb in enumerate(symbols):
			if start > i:
				operations.append(symb)
			if is_var(symb):
				is_started = True
			if symb == '(':
				bal += 1
			if symb == ')':
				bal -= 1
			if bal == 0 and is_started:
				parts.append(symbols[start: i + 1])
				start = i + 2
				is_started = False
				bal = 0 
		if len(operations) == 0:
			if (parts[0][0] == '~'):
				return Node(operation='~', 
					        leftson=self.__parse(parts[0][1:])
					        )
			return self.__parse(parts[0][1:-1])
		return self.__parts_parse(operations, parts)


	def __put_brackets(self, node: Node, operation: str) -> bool:
		if (node.var != None):
			return False
		return get_priority(node.operation) < get_priority(operation)
	