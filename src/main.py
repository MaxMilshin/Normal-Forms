from parser import Parser 
from converter import Converter

def main():
	# inputstr = input()
	# parser = Parser()
	# tree = parser.parse(inputstr)
	# nnf_tree = tree.convert_to_NNF()
	# result = parser.unparse(tree)
	# nnf_result = parser.unparse(nnf_tree)
	# print(result)
	# print(nnf_result)
	inputstr = input()
	converter = Converter()
	print(converter.convert_to_NNF(inputstr))
	print(converter.convert_to_DNF(inputstr))

if __name__ == "__main__":
	main()

# ~(x | ~y) & (x & ~y)
# (x & y) | (~x & ~y)

# ~~~~(x | y) & (x | ~y)
