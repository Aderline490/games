import turtle

wn = turtle.Screen()
wn.title("Pong By Aderline")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a

# Paddle B
paddle_b = turle.Turtle()

# Ball


# main game loop
while True:
    wn.update()