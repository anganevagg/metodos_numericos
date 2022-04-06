from sympy import Derivative, Function, diff, difference_delta, differentiate_finite, symbols, Eq
import sympy
from sympy.abc import x, y

def metodo_raphson_newton():
	n = 100
	f = input("f(x) = ")
	xn = float(input("x(0) = "))

	f = sympy.parse_expr(f, transformations='all')

	values = [xn]
	errors = []

	for v in range(0, n):
		xn = xn - (f/f.diff(x)).subs(x, xn)
		values.append(xn)
		errors.append(abs((values[v]-values[v-1])/values[v])*100)
		if(abs((values[v]-values[v-1])/values[v])*100<=0.00000001):
			break

	ant = values[0]

	print(values)
	errors.pop(0)
	# Printing results
	print("i	n	xn	er")
	for i in range(0, len(errors)):
		if(i==len(values)-1):
			print(f"{i}	x{i}	{values[i]}	")
		else:
			print(f"{i}	x{i}	{values[i]}	{errors[i]}")

	print(f"y = {f.subs(x, values[-1])}")