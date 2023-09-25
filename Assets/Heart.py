import turtle
import time

writetool= turtle.Turtle()

def cruve():
    for i in range(200):
        writetool.right(1)
        writetool.forward(1)

def heart():

    writetool.fillcolor('red')
    writetool.begin_fill()

    writetool.left(140)
    writetool.forward(113)

    cruve()
    writetool.left(120)

    cruve()
    writetool.forward(112)

    writetool.end_fill()

def text():

    writetool.setpos(-69, -25)
    writetool.down()

    writetool.color('blue')

    writetool.write("Hey", font=("roboto", 18, "bold"))

heart()
text()
time.sleep(1000)