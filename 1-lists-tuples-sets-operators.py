#Exemplo com listas ,tuplas ,conjuntos ,operadores  
# uma lista dé uma coleção de ordenada e mutavel
print("------------------------")
print ("Lista de coleçao ordenada e mutavel")
print("------------------------")
numeros = []
letras = []
mistura = []
print("lista de numeros ", numeros )
print("lista de letras ", letras )
print("lista de mistura ", mistura )


################################################################
# add a number to the 'numeros' list and then modify it
################################################################
print("------------------------")
print ("adicionando e modificando itens na lista")
print("------------------------")
numeros.append(4)
numeros[0] = 99
print("Lista alterada", numeros)



#################################
#Tuplas
################################
print("------------------------")
print ("#Tuplas")
print("------------------------")
Tupla = ("what","who","where",)
print ("tupla: ", Tupla) 

#################################################################
#um set é uma coleção não ordenada e não permite itens duplicados
#################################################################
print("------------------------")
print ("#um set é uma coleção não ordenada e não permite itens duplicados")
print("------------------------")
frutas = {"maça","banana","laranja","maça"}
print ("set sem duplicatas", frutas)
frutas.add ("banana")
print ("set apos add :",frutas)
#################################################################
#----------------Fozen set --------------------------------
#################################################################
print("------------------------")
print ("Fozen set")
print("------------------------")
conjunto = frozenset (["batata","alface","uva"])
print ("frozenset :",conjunto)

#------------> numericos !!!!! <----------------

############################
#Operação entre setas 
############################
print("------------------------")
print ("Operação entre setas ")
print("------------------------")
a = {1,2,3} 
b = {3,4,5}

#junção 
print ("uniao de a com b :",a|b )
#
print ("interseçãqo :", a & b )
#
print ("diferença", a-b)

print("------------------------")
#########################################
 # operadores 
 #  x == y, x!=y , x>y ,x<y, x>=y, x<=y
#########################################

print ("operadores")
print("------------------------")

x,y = 10,5
print ("x=",x ,"y=",y )
print ("x igualdade y", x == y)  
print ("x diferente y " ,x!=y)  
print ("x mairo que y ",x>y)  
print (" x menor que y ",x<y)  
print ("x menor ou igual que y",x<=y) 
print ("x maior ou igual que y",x>=y) 
print("------------------------")
#########################################
# Operadores aritméticos
#########################################
print ("Operadores aritméticos")
print("------------------------")
print("soma =",5 + 2)   # Soma → 7
print("Subtração =",5 - 2)   # Subtração → 3
print("multiplicação =",2 * 5)   # Multiplicação → 10
print("divisão =",5 / 2)   # Divisão → 2.5
print("Divisão inteira =",5 // 2)  # Divisão inteira → 2
print("resto da divisão =",5 % 2)   # Resto da divisão → 1
print("potencia =",5 ** 2)  # Potência → 25

print("------------------------")
#########################################
# Operadores lógicos
#########################################
print ("Operadores lógicos")
print("------------------------")
p, q = True, False

print("p and q:", p and q)  # AND lógico
print("p or q:", p or q)    # OR lógico
print("not p:", not p)      # NOT lógico
print("------------------------")