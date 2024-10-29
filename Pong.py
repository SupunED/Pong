import turtle
import winsound

# Window setup
window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)  # stops window from updating

# Score
scoreA = 0
scoreB = 0

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("light blue")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("yellow")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2  # fixed speed in the x direction
ball.dy = 0.2  # fixed speed in the y direction

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 20, "normal"))

# Paddle movement functions
def paddleA_up():
    y = paddleA.ycor()
    if y < 250:  # boundary check
        y += 20
    paddleA.sety(y)

def paddleA_down():
    y = paddleA.ycor()
    if y > -240:  # boundary check
        y -= 20
    paddleA.sety(y)

def paddleB_up():
    y = paddleB.ycor()
    if y < 250:  # boundary check
        y += 20
    paddleB.sety(y)

def paddleB_down():
    y = paddleB.ycor()
    if y > -240:  # boundary check
        y -= 20
    paddleB.sety(y)

# Keyboard bindings
window.listen()
window.onkeypress(paddleA_up, "w")
window.onkeypress(paddleA_down, "s")
window.onkeypress(paddleB_up, "Up")
window.onkeypress(paddleB_down, "Down")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking for top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = -ball.dy
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = -ball.dy
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)

    # Border checking for left and right (scoring)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = -ball.dx
        scoreA += 1
        pen.clear()
        pen.write(f"Player A: {scoreA}  Player B: {scoreB}", align="center", font=("Courier", 20, "normal"))
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = -ball.dx
        scoreB += 1
        pen.clear()
        pen.write(f"Player A: {scoreA}  Player B: {scoreB}", align="center", font=("Courier", 20, "normal"))
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)

    # Paddle and ball collision checking
    if (330 < ball.xcor() < 340) and (paddleB.ycor() - 50 < ball.ycor() < paddleB.ycor() + 50):
        ball.setx(330)
        ball.dx = -ball.dx
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)

    if (-340 < ball.xcor() < -330) and (paddleA.ycor() - 50 < ball.ycor() < paddleA.ycor() + 50):
        ball.setx(-330)
        ball.dx = -ball.dx
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)
