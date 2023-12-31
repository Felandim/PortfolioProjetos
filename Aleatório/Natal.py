import turtle

# Configurar a tela
tela = turtle.Screen()
tela.title("Árvore de Natal")
tela.bgcolor("white")

# Configurar a tartaruga
t = turtle.Turtle()
t.color("green")
t.shape("turtle")
t.speed(2)

# Função para desenhar um triângulo (parte da folhagem)
def desenha_triangulo():
    t.begin_fill()
    for _ in range(3):
        t.forward(100)  # Tamanho do lado do triângulo
        t.left(120)
    t.end_fill()

# Desenhar a árvore
t.penup()
t.goto(-50, -50)  # Posição inicial
t.pendown()
desenha_triangulo()  # Desenhar a base da árvore

t.penup()
t.goto(-40, -20)
t.pendown()
desenha_triangulo()  # Camada do meio

t.penup()
t.goto(-30, 10)
t.pendown()
desenha_triangulo()  # Topo da árvore

# Desenhar o tronco da árvore
t.color("brown")
t.penup()
t.goto(-15, -70)
t.pendown()
t.begin_fill()
for _ in range(2):
    t.forward(30)
    t.right(90)
    t.forward(20)
    t.right(90)
t.end_fill()

# Finalizar
t.hideturtle()
tela.mainloop()
