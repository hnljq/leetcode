from typing import List


def sum(x: List):
    if len(x) == 0:
        return None
    elif len(x) == 1:
        return x[0]
    else:
        return x[0] + sum(x[1:])


def num(x:List):
    if len(x) == 0:
        return None
    elif len(x) == 1:
        return 1
    else:
        return 1 + num(x[1:])


def max(x: List):
	if len(x) == 0:
		return None
	elif len(x) == 1:
		return x[0]
	elif len(x) == 2:
		if x[0]>= x[1]:
			return x[0]
		else:
			return x[1]
	else:
		


if __name__ == '__main__':
    l = [1,233,3]
    print(num(l))