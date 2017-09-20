from Nodo import *
from cola import *
class Arbol:
	def __init__(self):
		
		self.lista=[]
	def ecuacion(self, lis):
		self.lista=lis
		
	def llenar(self, Lista,Arbol):
		if Lista.numElem()>0:
			if Arbol==None:
				Arbol=Nodo(None)
				self.llenar(Lista, Arbol)
			else:
				if self.Tipo(Lista.primero()) ==1: #valor entero
					Arbol.valor=int(Lista.primero())
					Lista.sacar()
				elif self.Tipo(Lista.primero()) ==0:
					Arbol.valor=Lista.primero()
					Lista.sacar()
					Arbol.Izquierdo=Nodo(None)
					self.llenar(Lista, Arbol.Izquierdo)
					Arbol.Derecho=Nodo(None)
					self.llenar(Lista, Arbol.Derecho)
				elif self.Tipo(Lista.primero()) ==2 :
					cont=0
					while self.lista[cont][0] != Lista.primero():
						cont+=1
					num= self.lista[cont][1]                                        
					Arbol.valor=num
					Lista.sacar()
		return Arbol



	def Tipo(self,valor):# 0 operaciones 1 numero entero 2 paila
		if valor=='+':
			numero=0
		elif valor=='-':
			numero=0
		elif valor=='/':
			numero=0
		elif valor=='*':
			numero=0
		else:
			numero=2
			try:
				num= int(valor)
				numero=1
			except Exception as e:
				
				print ("")
		return numero
	
	def evaluar(self,arbol):
		if arbol.valor=='+':
			return self.evaluar(arbol.Izquierdo)+ self.evaluar(arbol.Derecho)
		elif arbol.valor=='-':
			return self.evaluar(arbol.Izquierdo)- self.evaluar(arbol.Derecho)
		elif arbol.valor=='/':
			return self.evaluar(arbol.Izquierdo)/ self.evaluar(arbol.Derecho)
		elif arbol.valor=='*':
			return self.evaluar(arbol.Izquierdo)* self.evaluar(arbol.Derecho)
		else: return arbol.valor

	
#[3,2,"+",5,8,"-","+","A"]
#[5,6,"+","B"]
#["B","+",5,6]
#[A[0],B[0],"-","C"]
cola = Cola()
valor=""
ecuaciones=[]
numEcu = input("numero de ecuaciones")
cont=0

while cont < numEcu:
	valor= raw_input("ingrese l expresion en prefijo: ").split(" ")
	i=0
	while i < len(valor) :
		cola.meter(valor[i])
		i+=1
	cola.sacar()    
	nombreEcu=cola.primero()
	cola.sacar()
	arbol = Arbol()
	arbol.ecuacion(ecuaciones)
	eucalipto=arbol.llenar(cola,None)
	ecuaciones.append([nombreEcu,arbol.evaluar(eucalipto)])
	print(nombreEcu + " = " + str(ecuaciones[cont]))
	valor=""
	cont+=1

