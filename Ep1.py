import turtle

print("""
	Exemplo:
	Condição inicial: F-F-F-F
	Produção: F F+F-FFF-
	Interação: 4
	""")

#primeira parte
primeira_fase = str(input("Condição inicial: "))
segunda_fase = str(input("Produção: "))
terceira_fase = int(input("Caminho: "))
fase_final = " "

segunda_fase = segunda_fase.split(' ') #para separar a string dada pelo usuário
fase_final = fase_final.upper()
#Segunda parte: aplicar regra de produção
i = 0
while i < terceira_fase:
    fase_final = primeira_fase.replace(segunda_fase[0], segunda_fase[1])
    primeira_fase = fase_final
    i=i+1




#Terceira parte: exibir regra final com a tartaruga
tartaruga = turtle.Turtle() 
tartaruga = turtle.Turtle() 
tartaruga.speed(500)
tartaruga.color("red")

for animal in fase_final: 
	if animal == 'F':
		tartaruga.pendown()
		tartaruga.forward(10)

	elif animal == '+':
		tartaruga.right(90)
		tartaruga.forward(10)

	elif animal == '-':
		tartaruga.left(90)
		tartaruga.forward(10)


window = turtle.Screen()   
window.bgcolor("white")
window.title("Fractais")
