"""
Universidad Nacional Autonoma de México
Mayo 2019
Matemáticas Aplicadas y computacion
By: Alexander Ordoñez Guido
La libreria scipy. interpolate nos ayuda a obtener el metodo de 
lagrange sin necesidad de ingresar más codigo. Ya viene por defecto 
en el lenguaje
La libreria matplotlib.pyplot nos grafica las funciones o en este
caso el polinomio resultante.
El modulo os hace posible el manejo de funciones dependientes del sistema oerativo
busca un módulo interno en función al SO del ordenador y luego exporta la misma 
funcionalidad para así ejecutar las acciones necesarias dentro del programa.
"""
from scipy.interpolate import lagrange 
import matplotlib.pyplot as plt
import os
cadena = "Polinomio de Lagrange" #creamos una cadena 
"""
Centramos el Titulo, lo equivalente a \t en c, 
longitud de 50 y - para mostrar un caracter en
el lugar vacio
"""

#función para sacar polinomios
def diferencias(k,x1,x2,y,y2):
	for i in range(0,k):
		vx=float(x1[i])#valor de equis
		x2.append(vx)#Guardamos los valores que intruduce el usuario en x=[]
		vfx=float(y[i])#valor de y
		y2.append(vfx)#Guardamos los valores que intruduce el usuario en y=[]

print (cadena.center(50, "-")) 
print("\n")#salto de linea 
x1=[] 
y=[]
x2=[]
y2=[]
x3=[]
y3=[]
x4=[]
y4=[]
x5=[]
y5=[]
x6=[]
y6=[]
x7=[]
y7=[]
x8=[]
y8=[]
x9=[]
y9=[]
comprobar = True #comprobaremos si k es > 0
while comprobar == True: # While servirá para iniciar nuevamente el programa en caso de que el usuario intriduzca un k erroneo 
	k=int(input("Ingresa el Numero de iteraciones: "))	
	if k>2 and k<=10:
		comprobar = False #hacemos falso para hacer que el bucle se detenga cuando la condicion se cumppla
	else:
		print("El número que ingresaste no es correcto, intenta de nuevo")
print("El rango hace referencia al conjunto de valores que puede tomar x")
c=int(input("Rango inicial de x: "))
s=int(input("Puntos final de x: "))
for i in range(0,k):
	vx=float(input("x"+str(i+1)+": "))#valor de equis
	x1.append(vx)#Guardamos los valores que intruduce el usuario en x=[]
	vfx=float(input("f(x)"+str(i+1)+": "))#valor de y
	y.append(vfx)#Guardamos los valores que intruduce el usuario en y=[]				
print("prueba")
w=float(input("Evaluar a x en: "))		
os.system ("clear")#limpiamos pantalla
print(cadena.center(50, "-"))
print("\n")
#creamos una tabla para imprimir los valores del arreglo sin [] y en orden introducidos por el usuario
sep='|{}|{}|'.format('-'*16,  '-'*10)
print('{0}\n|        x       |   f(x)   |\n{0}'.format(sep))
for cal, cred in zip(x1,y):
	print('| {:>14.2f} | {:>8.2f} |\n{}'.format(cal, cred,  sep))
print('\n')
if k==2:
	#Polonimoios imprimir
	k=k-1
	diferencias(k,x1,x2,y,y2)#Copiamos los datos de x1 y y en x2 y y2
	print("\t Polinomios \n")
	p10=lagrange(x1,y)  #Aplicamos lagrange para x1,y
	p9=	lagrange(x2,y2)	#Aplicamos lagrange para x1,y	
	print("Polinomio grado 2: \n\n",p10)		
	plt.plot(x1,y,"o") #imprimimos los putos x1 y y en la grafica
	plt.xlabel("x") #graficamos x
	plt.ylabel("y") #graficamos y 
	x=range(c,s)  #creamos un rango para el plano xy
	plt.plot(x,[p10(i) for i in x]) #graficamos el polinomio p10 guardado en lagrange
	plt.show() #muestra la grafica



if k==3:
	k=k-1
	diferencias(k,x1,x2,y,y2)
	k=k-1
	diferencias(k,x2,x3,y2,y3)
	print("\t Polinomios \n")
	p10=lagrange(x1,y)
	p9=	lagrange(x2,y2)		
	print("Polinomio grado 1: \n\n",p9)	
	print("Polinomio grado 2: \n\n",p10)		
	plt.plot(x1,y,"o")
	plt.xlabel("x")
	plt.ylabel("y")
	x=range(c,s)
	plt.plot(x,[p9(i) for i in x])
	plt.plot(x,[p10(i) for i in x])


	plt.show()



if k==4:
	k=k-1
	diferencias(k,x1,x2,y,y2)
	k=k-1
	diferencias(k,x2,x3,y2,y3)
	k=k-1
	diferencias(k,x3,x4,y3,y4)	
	print("\t Polinomios \n")
	p10=lagrange(x1,y)
	p9=	lagrange(x2,y2)	
	p8=	lagrange(x3,y3)		
	print("Polinomio grado 1: \n\n",p8)
	print("Polinomio grado 2: \n\n",p9)	
	print("Polinomio grado 3: \n\n",p10)		
	plt.plot(x1,y,"o")
	plt.xlabel("x")
	plt.ylabel("y")
	x=range(c,s)
	plt.plot(x,[p8(i) for i in x])
	plt.plot(x,[p9(i) for i in x])
	plt.plot(x,[p10(i) for i in x])


	plt.show()




if k==5:
	k=k-1
	diferencias(k,x1,x2,y,y2)
	k=k-1
	diferencias(k,x2,x3,y2,y3)
	k=k-1
	diferencias(k,x3,x4,y3,y4)
	k=k-1
	diferencias(k,x4,x5,y4,y5)		
	print("\t Polinomios \n")
	p10=lagrange(x1,y)
	p9=	lagrange(x2,y2)	
	p8=	lagrange(x3,y3)
	p7=	lagrange(x4,y4)		
	print("Polinomio grado 1: \n\n",p7)
	print("Polinomio grado 2: \n\n",p8)
	print("Polinomio grado 3: \n\n",p9)	
	print("Polinomio grado 4: \n\n",p10)		
	plt.plot(x1,y,"o")
	plt.xlabel("x")
	plt.ylabel("y")
	x=range(c,s)
	plt.plot(x,[p7(i) for i in x])
	plt.plot(x,[p8(i) for i in x])
	plt.plot(x,[p9(i) for i in x])
	plt.plot(x,[p10(i) for i in x])


	plt.show()




if k==6:
	k=k-1
	diferencias(k,x1,x2,y,y2)
	k=k-1
	diferencias(k,x2,x3,y2,y3)
	k=k-1
	diferencias(k,x3,x4,y3,y4)
	k=k-1
	diferencias(k,x4,x5,y4,y5)
	k=k-1
	diferencias(k,x5,x6,y5,y6)		
	print("\t Polinomios \n")
	p10=lagrange(x1,y)
	p9=	lagrange(x2,y2)	
	p8=	lagrange(x3,y3)
	p7=	lagrange(x4,y4)
	p6=	lagrange(x5,y5)		
	print("Polinomio grado 1: \n\n",p6)
	print("Polinomio grado 2: \n\n",p7)
	print("Polinomio grado 3: \n\n",p8)
	print("Polinomio grado 4: \n\n",p9)	
	print("Polinomio grado 5: \n\n",p10)		
	plt.plot(x1,y,"o")
	plt.xlabel("x")
	plt.ylabel("y")
	x=range(c,s)
	plt.plot(x,[p6(i) for i in x])
	plt.plot(x,[p7(i) for i in x])
	plt.plot(x,[p8(i) for i in x])
	plt.plot(x,[p9(i) for i in x])
	plt.plot(x,[p10(i) for i in x])


	plt.show()




if k==7:
	k=k-1
	diferencias(k,x1,x2,y,y2)
	k=k-1
	diferencias(k,x2,x3,y2,y3)
	k=k-1
	diferencias(k,x3,x4,y3,y4)
	k=k-1
	diferencias(k,x4,x5,y4,y5)
	k=k-1
	diferencias(k,x5,x6,y5,y6)
	k=k-1
	diferencias(k,x6,x7,y6,y7)
	print("\t Polinomios \n")
	p10=lagrange(x1,y)
	p9=	lagrange(x2,y2)	
	p8=	lagrange(x3,y3)
	p7=	lagrange(x4,y4)
	p6=	lagrange(x5,y5)
	p5=	lagrange(x6,y6)
	print("Polinomio grado 1: \n\n",p5)		
	print("Polinomio grado 2: \n\n",p6)
	print("Polinomio grado 3: \n\n",p7)
	print("Polinomio grado 4: \n\n",p8)
	print("Polinomio grado 5: \n\n",p9)	
	print("Polinomio grado 6: \n\n",p10)		
	plt.plot(x1,y,"o")
	plt.xlabel("x")
	plt.ylabel("y")
	x=range(c,s)
	plt.plot(x,[p5(i) for i in x])
	plt.plot(x,[p6(i) for i in x])
	plt.plot(x,[p7(i) for i in x])
	plt.plot(x,[p8(i) for i in x])
	plt.plot(x,[p9(i) for i in x])
	plt.plot(x,[p10(i) for i in x])


	plt.show()





if k==8:
	k=k-1
	diferencias(k,x1,x2,y,y2)
	k=k-1
	diferencias(k,x2,x3,y2,y3)
	k=k-1
	diferencias(k,x3,x4,y3,y4)
	k=k-1
	diferencias(k,x4,x5,y4,y5)
	k=k-1
	diferencias(k,x5,x6,y5,y6)
	k=k-1
	diferencias(k,x6,x7,y6,y7)
	k=k-1
	diferencias(k,x7,x8,y7,y8)
	print("\t Polinomios \n")
	p10=lagrange(x1,y)
	p9=	lagrange(x2,y2)	
	p8=	lagrange(x3,y3)
	p7=	lagrange(x4,y4)
	p6=	lagrange(x5,y5)
	p5=	lagrange(x6,y6)
	p4=	lagrange(x7,y7)
	print("Polinomio grado 1: \n\n",p4)
	print("Polinomio grado 2: \n\n",p5)		
	print("Polinomio grado 3: \n\n",p6)
	print("Polinomio grado 4: \n\n",p7)
	print("Polinomio grado 5: \n\n",p8)
	print("Polinomio grado 6: \n\n",p9)	
	print("Polinomio grado 7: \n\n",p10)		
	plt.plot(x1,y,"o")
	plt.xlabel("x")
	plt.ylabel("y")
	x=range(c,s)
	plt.plot(x,[p4(i) for i in x])
	plt.plot(x,[p5(i) for i in x])
	plt.plot(x,[p6(i) for i in x])
	plt.plot(x,[p7(i) for i in x])
	plt.plot(x,[p8(i) for i in x])
	plt.plot(x,[p9(i) for i in x])
	plt.plot(x,[p10(i) for i in x])


	plt.show()





if k==9:
	k=k-1
	diferencias(k,x1,x2,y,y2)
	k=k-1
	diferencias(k,x2,x3,y2,y3)
	k=k-1
	diferencias(k,x3,x4,y3,y4)
	k=k-1
	diferencias(k,x4,x5,y4,y5)
	k=k-1
	diferencias(k,x5,x6,y5,y6)
	k=k-1
	diferencias(k,x6,x7,y6,y7)
	k=k-1
	diferencias(k,x7,x8,y7,y8)
	k=k-1
	diferencias(k,x8,x9,y8,y9)
	print("\t Polinomios \n")
	p10=lagrange(x1,y)
	p9=	lagrange(x2,y2)	
	p8=	lagrange(x3,y3)
	p7=	lagrange(x4,y4)
	p6=	lagrange(x5,y5)
	p5=	lagrange(x6,y6)
	p4=	lagrange(x7,y7)
	p3=	lagrange(x8,y8)
	print("Polinomio grado 1: \n\n",p3)
	print("Polinomio grado 2: \n\n",p4)
	print("Polinomio grado 3: \n\n",p5)		
	print("Polinomio grado 4: \n\n",p6)
	print("Polinomio grado 5: \n\n",p7)
	print("Polinomio grado 6: \n\n",p8)
	print("Polinomio grado 7: \n\n",p9)	
	print("Polinomio grado 8: \n\n",p10)		
	plt.plot(x1,y,"o")
	plt.xlabel("x")
	plt.ylabel("y")
	x=range(c,s)
	plt.plot(x,[p3(i) for i in x])
	plt.plot(x,[p4(i) for i in x])
	plt.plot(x,[p5(i) for i in x])
	plt.plot(x,[p6(i) for i in x])
	plt.plot(x,[p7(i) for i in x])
	plt.plot(x,[p8(i) for i in x])
	plt.plot(x,[p9(i) for i in x])
	plt.plot(x,[p10(i) for i in x])


	plt.show()	
    




if k==10:
	k=k-1
	diferencias(k,x1,x2,y,y2)
	k=k-1
	diferencias(k,x2,x3,y2,y3)
	k=k-1
	diferencias(k,x3,x4,y3,y4)
	k=k-1
	diferencias(k,x4,x5,y4,y5)
	k=k-1
	diferencias(k,x5,x6,y5,y6)
	k=k-1
	diferencias(k,x6,x7,y6,y7)
	k=k-1
	diferencias(k,x7,x8,y7,y8)
	k=k-1
	diferencias(k,x8,x9,y8,y9)
	print("\t Polinomios \n")
	p10=lagrange(x1,y)
	p9=	lagrange(x2,y2)	
	p8=	lagrange(x3,y3)
	p7=	lagrange(x4,y4)
	p6=	lagrange(x5,y5)
	p5=	lagrange(x6,y6)
	p4=	lagrange(x7,y7)
	p3=	lagrange(x8,y8)
	p2=	lagrange(x9,y9)
	print("Polinomio grado 1: \n\n",p2)
	print("Polinomio grado 2: \n\n",p3)
	print("Polinomio grado 3: \n\n",p4)
	print("Polinomio grado 4: \n\n",p5)		
	print("Polinomio grado 5: \n\n",p6)
	print("Polinomio grado 6: \n\n",p7)
	print("Polinomio grado 7: \n\n",p8)
	print("Polinomio grado 8: \n\n",p9)	
	print("Polinomio grado 9: \n\n",p10)		
	plt.plot(x1,y,"o")
	plt.xlabel("x")
	plt.ylabel("y")
	x=range(c,s)		
	plt.plot(x,[p2(i) for i in x])
	plt.plot(x,[p3(i) for i in x])
	plt.plot(x,[p4(i) for i in x])
	plt.plot(x,[p5(i) for i in x])
	plt.plot(x,[p6(i) for i in x])
	plt.plot(x,[p7(i) for i in x])
	plt.plot(x,[p8(i) for i in x])
	plt.plot(x,[p9(i) for i in x])
	plt.plot(x,[p10(i) for i in x])


	plt.show()		
