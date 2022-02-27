def is_var(a: str) -> bool:
	return a not in ['(', ')', '&', '|', '~']

def is_var_char(a: str) -> bool:
	return a >= 'a' and a <= 'z'

def get_priority(a: str) -> int:
	if (a == '~'):
		return 3
	if (a == '&'):
		return 2
	if (a == '|'):
		return 1
