import math
class QuadEquation:
    """description of class"""


def Equation(a, b, c):
    error = ''
    answer = []
    if a == 0:
	    if b == 0:
		    if c == 0:
			    error = 'R'
			    answer = []
		    else:
			    error = 'Нет корней'
			    answer = []
	    else:
		    answer = [ -c / b ]
    else:
	    d = b ** 2 - 4 * a * c
	    if d > 0:
		    answer = [ (-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a) ]
	    elif d == 0:
		    answer = [ -b / (2 * a) ]
	    else:
		    error = 'Нет корней'
		    answer = []
    return error, answer

