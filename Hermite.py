"""
Universidad Nacional Autonoma de México
Mayo 2019
Matemáticas Aplicadas y computacion
By: Alexander Ordoñez Guido
"""
import os
cadena = "Polinomio de Hermite"
print(cadena.center(50, "-"))
print("\n")#salto de linea
x=[]
fx=[]
fpx=[]
l=[]
m=[]
n=[]
o=[]
p=[]
comprobar = True
while comprobar==True:
	k=int(input("Ingresa el Número de iteraciones: \n"))
	if k>=2 and k<=10:
		comprobar=False
	else:
		print("El número que ingresaste no es correcto, intenta de nuevo \n")
print("El rango hace referencia al conjunto de valores que puede tomar x \n")	
c=int(input("Rango incial de x: \n"))
s=int(input("Rango final de x: \n"))
for i in range(0,k):
	vx=float(input("x"+str(i+1)+": "))#Valor de x
	x.append(vx)#Guardamos los valores que introduce el usuario en x[]
	vfx=float(input("f(x)"+str(i+1)+": "))#valor de fx
	fx.append(vfx)
	vfpx=float(input("f'(x)"+str(i+1)+": "))#valor de fpx
	fpx.append(vfpx)#guardamos vfpx en fpx[]
w=float(input("Evaluar a x en: "))
os.system("clear")#limpiamos pantalla
print(cadena.center(50,"-"))
for i in range(0,k-1):# utilizamos un for para la formula en k casos
	b1=float((fx[i+1]-fx[i])/(x[i+1]-x[i]))
	l.append(b1)#guardamos los datos en l[]
print("\n")
sep='|{}|{}|{}|'.format('-'*16,'-'*16,'-'*16)
print('{0}\n|        x       |     f(x)       |       f'"'"'(x)    |\n{0}'.format(sep))
for cal,cred,crow in zip(x,fx,fpx):
	print('| {:>14} | {:>14} | {:>14} |\n{}'.format(cal,cred,crow,sep))
print("\n")
print("El valor de la primera es: ",', '.join(map(str, l))) #Valores de la primera iteracion
print("\n")
for i in range(0,k-1):
	b2=float((l[i]-fpx[i])/(x[i+1]-x[i]))
	m.append(b2)
	b3=float((fpx[i+1]-l[i])/(x[i+1]-x[i]))
	m.append(b3)
print("El valor de la segunda es: ",', '.join(map(str, m))) #valores de la segunda iteracion
print("\n")
for i in range(0,k-2):
	#tercera
	b4=float((m[i+1]-m[i])/(x[i+1]-x[i]))
	n.append(b4)
	b5=float((m[i+2]-m[i+1])/(x[i+2]-x[i]))
	n.append(b5)
	b6=float((m[i+3]-m[i+2])/(x[i+2]-x[i+1]))
	n.append(b6)
	#cuarta
	b7=float((n[i+1]-n[i])/(x[i+2]-x[0]))
	o.append(b7)
	b8=float((n[i+2]-n[i+1])/(x[i+2]-x[0]))
	o.append(b8)
	#quinta
	b9=float((o[i+1]-o[i])/(x[i+2]-x[i]))
	p.append(b9)
print("El valor de la tercera es: ",', '.join(map(str, n))) #valores de la terera iteracion
print("\n")
print("El valor de la cuarta es: ",', '.join(map(str, o))) #valores de la cuarta iteracion
print("\n")
print("El valor de la quinta es: ",', '.join(map(str, p))) #valores de la quinta iteracion
print("\n")#()
print("Polinomio \n")
polinomio=float(fx[0]+((w*k)-x[0])*fpx[0]+((w*k)-x[0])*((w*k)-x[0])*m[0]+((w*k)-x[0])*((w*k)-x[0])*((w*k)-x[1])*n[0]+((w*k)-x[0])*((w*k)-x[0])*((w*k)-x[1])*((w*k)-x[1])*o[0]+((w*k)-x[0])*((w*k)-x[1])*((w*k)-x[1])*((w*k)-x[2])*((w*k)-x[2])*p[0])
#polinomio2=float(((w*k)-x[0])*((w*k)-x[0])*((w*k)-x[2])*((w*k)-x[3])) #(((w*k)-x[0])*((w*k)-x[1])*((w*k)-x[2])*((w*k)-x[3])*o[0])
#+((w*k)-x[1])*((w*k)-x[2])*((w*k)-x[3])*((w*k)-x[4])*((w*k)-x[5])*p[0])
print(polinomio)
print("\n")
#print(polinomio2)



