import math

if __name__ == '__main__':
    suma = lambda x,y:x+y
    resultado = suma(3,4)

    resta = lambda x,y:x-y
    resultado = resta(3,4)

    potencia = lambda x:x**2
    resultado = potencia(9)

    x1= lambda a,b,c:(-b+math.sqrt(b**2*4*a*c))/(2*a)