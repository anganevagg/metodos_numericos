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
	yn=y0

	n=int((xf)/h)+1

	func = input("y = ")

	func = sympy.parse_expr(func, transformations='all')

	xv = np.zeros(n)
	yv = np.zeros(n)
	ys = np.zeros(n)

	dy=dsolve(sympy.Eq(f(x).diff(x), func.subs(y, f(x))))
	print(sympy.Eq(f(x).diff(x), func.subs(y, f(x))))

	cte=solve(dy.subs(f(x), y0).subs(x, x0))

	print(dy.lhs)
	print(cte)

	xv[0] = x0
	yv[0] = y0

	for i in range(1, n):
		xv[i] = xv[0]+i*h
		#print(dy.subs(x, xv[i]).subs(c1, cte[0]))
		print(dy)

	print(xv)
	print(yv)