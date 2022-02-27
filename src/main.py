import sys

from parser import Parser 
from converter import Converter

def main():
	form = sys.argv[1]
	inputstr = input()
	converter = Converter()
	if form == 'NNF':
		print(converter.convert_to_NNF(inputstr))
	if form == 'DNF':
		print(converter.convert_to_DNF(inputstr))
	if form == 'CNF':
		print(converter.convert_to_CNF(inputstr))

if __name__ == "__main__":
	main()
