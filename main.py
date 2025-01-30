from turtle import Turtle, Screen

"""Create a event listener that:
 - W allows to move forward
 - S allows you to move backwards
 - A To go counter clockwise - left
 - D To go clockwise
 - C Clockwise

 """
tim = Turtle()

def moves_forward():
    tim.forward(50)
def moves_backward():
    tim.backward(50)

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

screen = Screen()
screen.listen() #listens to the key we input into the function to create an action
screen.onkey(key="w", fun=moves_forward)
screen.onkey(key="s", fun=moves_backward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=screen.clearscreen)
screen.exitonclick()


