import turtle

def draw_sierpinski(length, depth):

    if depth == 0:
        for _ in range(3):
            turtle.fillcolor('orange')
            turtle.begin_fill()
            turtle.forward(length)
            turtle.right(120)
            turtle.end_fill()
    else:
        draw_sierpinski(length / 2, depth - 1)
        turtle.forward(length / 2)
        draw_sierpinski(length / 2, depth - 1)
        turtle.backward(length / 2)
        turtle.right(60)
        turtle.forward(length / 2)
        turtle.left(60)
        draw_sierpinski(length / 2, depth - 1)
        turtle.left(60)
        turtle.backward(length / 2)
        turtle.right(60)

turtle.speed(0)
turtle.bgcolor('black')  # Set background color to black
turtle.color('white')  # Set pen color to white
draw_sierpinski(200, 4)
turtle.done()