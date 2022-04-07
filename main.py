from metodos.euler import metodo_euler
from metodos.interpolacion import metodo_interpolacion
from metodos.raphson_newton import metodo_raphson_newton
print("=======================Bienvenido a la calculadora de metodos numericos de LAS RATAS===========================")

print('Metodo de Euler:1\n')
print('Metodo de Interpolacion:2\n')
print('Metodo de Newton Raphson:3\n')
opcion=int(input("Selecciona el metodo \n"))


if opcion == 1:
        print('Metodo de Euler')
        metodo_euler()
else:
    if opcion == 2:
            print('Metodo de Interpolacion')
            metodo_interpolacion()
    else:
        if opcion == 3:
                print('Metodo de Newton Raphson')
                metodo_raphson_newton()
        else:
         print('error')