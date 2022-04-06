from sympy import Derivative, Function, Symbol, diff, difference_delta, differentiate_finite, dsolve, evaluate, fu, integrate, solve, symbols, Eq
import sympy
from sympy.parsing.sympy_parser import transformations as T
from sympy.abc import x, y

import numpy as np
import matplotlib as math


def metodo_euler():
	f = Function("f")

	x0=float(input("x0 = "))
	y0=float(input("y0 = "))
	xf=float(input("xf = "))
	h=float(input("h = "))

	n=int((xf-x0)/h)+1

	func = input("y = ")

	func = sympy.parse_expr(func, transformations='all')

	xv = np.zeros(n)
	yv = np.zeros(n)
	xv[0] = x0
	yv[0] = y0


	for i in range(1, n):
		xv[i] =	xv[0] + h*i
		yv[i] = yv[i-1] + h*func.subs(x, xv[i-1]).subs(y, yv[i-1])


	print(f"y = {yv[-1]}")