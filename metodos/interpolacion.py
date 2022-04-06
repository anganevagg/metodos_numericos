from cmath import inf

def metodo_interpolacion():
	inferior = [float(input("Ingresa el valor X inferior: ")), float(input("Ingresa el valor Y inferior: "))]
	superior = [float(input("Ingresa el valor X superior: ")), float(input("Ingresa el valor Y superior: "))]

	dx = inferior[0] - superior[0]
	dy = inferior[1] - superior[1]

	opcion = int(input("Ingrese 1 si va a entrar X\nIngrese 2 si va a entrar y\nR: "))

	if(opcion==2):
		x = float(input("Ingresa el valor a interpolar en X: "))
		dx2 = inferior[0] - x
		y = inferior[1]-(dy*dx2)/dx
		print(y)
	else:
		y = float(input("Ingresa el valor a interpolar en Y: "))
		dy2 = inferior[1] - y
		x = inferior[0]-(dx*dy2)/dy
		print(x)